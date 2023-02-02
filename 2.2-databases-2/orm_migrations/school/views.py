from django.views.generic import ListView
from django.shortcuts import render

from school.admin import StudentAdmin

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'
    students_QuerySet = Student.objects.all().order_by(ordering).prefetch_related("students")

    template = 'school/students_list.html'
    context = {"object_list": students_QuerySet}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
