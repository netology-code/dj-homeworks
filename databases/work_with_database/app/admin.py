from django.contrib import admin

from app.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)


admin.site.register(Phone, PhoneAdmin)
