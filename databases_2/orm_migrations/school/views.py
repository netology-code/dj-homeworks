from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'
