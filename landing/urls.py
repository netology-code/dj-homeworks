from django.contrib import admin
from django.urls import path

from landing.views import landing


urlpatterns = [
    path('', landing),
    path('admin/', admin.site.urls),
]
