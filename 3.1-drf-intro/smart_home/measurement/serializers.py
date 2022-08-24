from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'image', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'measurement_date']


class MeasurementForSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'measurement_date']


class SensorDetailsSerializer(serializers.ModelSerializer):
    measurements = MeasurementForSensorSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'image', 'description', 'measurements']