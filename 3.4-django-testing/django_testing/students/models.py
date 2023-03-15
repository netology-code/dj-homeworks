from django.db import models


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )

    def __str__(self):
        return self.name


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

    def __str__(self):
        return self.name
