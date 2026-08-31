from rest_framework import serializers


# TODO: опишите сериализатор датчика (ModelSerializer) для вывода id, name, description.

# TODO: опишите сериализатор измерения (ModelSerializer) для вывода temperature, created_at.

# TODO: опишите детальный сериализатор датчика (ModelSerializer):
# - поля: id, name, description, measurements;
# - measurements — вложенный сериализатор MeasurementSerializer(read_only=True, many=True).
