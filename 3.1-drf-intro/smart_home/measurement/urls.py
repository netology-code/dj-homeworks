from django.urls import path

from measurement.views import SensorsView, SensorView, MeasurementsView

urlpatterns = [
    path('sensors', SensorsView.as_view(), name='sensors'),
    path('sensors/<pk>', SensorView.as_view(), name='sensor'),
    path('measurements', MeasurementsView.as_view(), name='measurements')
    # TODO: зарегистрируйте необходимые маршруты
]
