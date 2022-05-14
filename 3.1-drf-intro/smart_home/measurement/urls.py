from django.urls import path

from measurement.views import SensorView, MeasurementCreate, SingleSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
]
