import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
    path('__debug__', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls)
]
