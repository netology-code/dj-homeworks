from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from .models import Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["temperature", "created_at"]

class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    measurements = MeasurementSerializer(many=True)

