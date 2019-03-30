from django.contrib import admin

# Register your models here.

import phones.models


@admin.register(phones.models.Processor)
class ProcessorAdmin(admin.ModelAdmin):
    pass


@admin.register(phones.models.ScreeenResolution)
class ScreeenResolutionAdmin(admin.ModelAdmin):
    pass


@admin.register(phones.models.DeviceOS)
class DeviceOSAdmin(admin.ModelAdmin):
    pass


@admin.register(phones.models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(phones.models.Camera)
class CameraAdmin(admin.ModelAdmin):
    pass


@admin.register(phones.models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

