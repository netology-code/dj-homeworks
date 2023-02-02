from django.contrib import admin

from .models import Student, Teacher, TeacherStudent

class TeacherStudentInline(admin.TabularInline):
    #model = Student.teachers.through
    model = TeacherStudent
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "group"]
    list_filter = ["name", "group"]
    inlines = [TeacherStudentInline,]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject"]
    list_filter = [ "name", "subject"]
    inlines = [TeacherStudentInline,]

