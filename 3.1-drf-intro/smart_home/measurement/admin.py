from django.contrib import admin

from measurement.models import Measurement, Sensor

class SensorMeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1

# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'date_create', 'date_update']
    list_filter = ['id', 'name', 'date_create', 'date_update', ]
    inlines = [SensorMeasurementInline, ]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at', 'image']
    list_filter = ['id', 'sensor', 'temperature']

