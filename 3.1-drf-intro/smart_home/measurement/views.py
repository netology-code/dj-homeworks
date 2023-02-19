
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer

@api_view(['POST'])
def demo2(request):
    sensor = Sensor.objects.get(id=request.data['sensor'])
    measurement = Measurement(sensor=sensor, temperature=request.data['temperature'])
    measurement.save()
    return Response({'status': "OK"})

@api_view(['GET', 'POST', 'PATCH'])
def demo1(request, sensor_id=0):
    if request.method == 'GET':
        if sensor_id == 0:
            sensors = Sensor.objects.all()
            ser = SensorSerializer(sensors, many=True)
            return Response(ser.data)
        if sensor_id > 0:
            sensor = Sensor.objects.get(id=sensor_id)
            ser = SensorDetailSerializer(sensor, many=False)
            return Response(ser.data)
    if request.method == 'POST':
        sensor = Sensor(name=request.data['name'], description=request.data['description'])
        sensor.save()
        return Response({'status': 'OK'})
    if request.method == 'PATCH':
        if sensor_id == 0:
            return Response({'status': 'Изменяемая запись не определена'})
        if sensor_id > 0:
            sensor = Sensor.objects.get(id=sensor_id)
            sensor.description = request.data['description']
            sensor.save()
            return Response({'status': 'OK'})

class DemoView(APIView):
    def get(self, request, sensor_id=0):
        if sensor_id == 0:
            sensors = Sensor.objects.all()
            ser = SensorSerializer(sensors, many=True)
            return Response(ser.data)
        if sensor_id > 0:
            sensor = Sensor.objects.get(id=sensor_id)
            ser = SensorDetailSerializer(sensor, many=False)
            return Response(ser.data)
    
    def post(self, request):
        sensor = Sensor(name=request.data['name'], description=request.data['description'])
        sensor.save()
        return Response({'status': 'POST OK'})
    
    def patch(self, request, sensor_id=0):
        if sensor_id == 0:
            return Response({'status': 'Изменяемая запись не определена'})
        if sensor_id > 0:
            sensor = Sensor.objects.get(id=sensor_id)
            sensor.description = request.data['description']
            sensor.save()
        return Response({'status': 'PATCH OK'})

class DemoViewMesuarement(APIView):
    def post(self, request):
        sensor = Sensor.objects.get(id=request.data['sensor'])
        measurement = Measurement(sensor=sensor, temperature=request.data['temperature'])
        measurement.save()
        return Response({'status': "OK"})