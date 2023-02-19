from rest_framework import serializers

from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'date_create', 'date_update']

class SensorDetailSerializer(serializers.ModelSerializer):
    sensor = MeasurementSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'date_create', 'date_update', 'sensor']