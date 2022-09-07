from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, Favorite


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class FavoriteSerializer(serializers.ModelSerializer):
    '''Serializer для избранного.'''

    class Meta:
        model = Favorite
        fields = ('id', 'owner', 'ad')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True, )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'draft')

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # Обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # Само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        request = self.context['request'].method
        user = self.context['request'].user
        # favorite = self.initial_data.get('favorites', False)

        if request == 'POST' and Advertisement.objects.filter(creator=user, status='OPEN').count() >= 10:
            raise ValidationError('You cannot create more than 10 open ads')

        # if favorite:
        #     if user == self.instance.creator:
        #         raise ValidationError('You cannot add your listings to favorites')
        #     data['favorites'] = [Favorite(self.context["request"].user, self.instance).save()]
        #     # data['favorites__ad'] = self.instance.pk
        #     k = 1

        return data
