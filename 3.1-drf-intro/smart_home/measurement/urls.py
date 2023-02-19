from django.urls import path

from measurement.views import DemoView, demo1, demo2, DemoViewMesuarement

#from measurement.views import demo

urlpatterns = [
    #path('sensors/<int:sensor_id>/', demo1),
    #path('sensors/', demo1),
    path('sensors/<int:sensor_id>/', DemoView.as_view()),
    path('sensors/', DemoView.as_view()),
    #path('measurements/', demo2),
    path('measurements/', DemoViewMesuarement.as_view())
]
