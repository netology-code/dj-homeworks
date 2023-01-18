from django.contrib import admin
from .models import Phone

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "image", "image_url", "release_date", "lte_exist", "slug"]
    list_filter = ["name", "price", "release_date", "lte_exist", "slug"]