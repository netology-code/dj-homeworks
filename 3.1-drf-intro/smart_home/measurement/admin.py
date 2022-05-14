from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement

admin.site.register(Sensor)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list = [Measurement.temperature, Measurement.created_at, Measurement.sensor]


