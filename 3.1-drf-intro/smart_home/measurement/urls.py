
from django.urls import path

from measurement.views import SensorListView, SensorDetailView, SensorUpdateView, SensorCreateView, \
    MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListView.as_view()),
    path('sensors/create/', SensorCreateView.as_view()),
    path('sensors/<pk>/update/', SensorUpdateView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/create/', MeasurementCreateView.as_view()),
]
