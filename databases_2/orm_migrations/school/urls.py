from django.urls import path

from .views import StudentListView

urlpatterns = [
    path('', StudentListView.as_view()),
]
