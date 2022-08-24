# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailsSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        title = request.data['name']
        description = request.data['description']
        image = request.data.get('image')
        sensor = Sensor.objects.create(title=title, image=image, description=description)
        return Response(f'Датчик {sensor} добавлен')


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        if request.data.get('description'):
            sensor.description = request.data['description']
        if request.data.get('title'):
            sensor.title = request.data['title']
        if request.data.get('image'):
            sensor.image = request.data['image']
        sensor.save()
        return Response(f'Датчик {sensor} изменён')


class MeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor = Sensor.objects.get(pk=request.data['sensor'])
        temperature = request.data['temperature']
        mes = Measurement.objects.create(sensor_id=sensor, temperature=temperature)
        return Response(f'{mes}. Измерение для датчика {sensor} добавлено')
