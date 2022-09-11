from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from students.filters import CourseFilter
from students.models import Course, Student
from students.serializers import CourseSerializer, StudentSerializer


class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter


class StudentsViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, )
    # filterset_class = CourseFilter