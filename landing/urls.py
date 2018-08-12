from django.urls import path

from landing.views import landing, stats


urlpatterns = [
    path('', landing),
    path('stats/', stats, name='stats'),
]
