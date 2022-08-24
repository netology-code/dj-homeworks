from django.contrib import admin

from measurement.models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 0


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'description']
    list_filter = ['title', 'description']
    inlines = [MeasurementInline, ]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor_id', 'temperature', 'measurement_date']
    list_filter = ['sensor_id', 'measurement_date']
