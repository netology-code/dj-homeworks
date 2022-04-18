from django.urls import path

from measurement.views import SensorView, SensorsView, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
]
