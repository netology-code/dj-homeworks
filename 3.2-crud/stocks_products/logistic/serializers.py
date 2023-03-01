from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price'] #'id', 

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            new_position = StockProduct.objects.create(
                product=position.get('product'),
                stock=stock,
                quantity=position.get('quantity'),
                price=position.get('price'))
            new_position.save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:                         # Проходимся по всем объектам данных из запроса
            product = position.get('product')              
            quantity = position.get('quantity')
            price = position.get('price')

            StockProduct.objects.update_or_create(
                stock=stock,
                product=product,
                defaults={'price': price,
                          'quantity': quantity}
            )

        return stock
