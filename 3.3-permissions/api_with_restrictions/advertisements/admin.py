from django.contrib import admin

from advertisements.models import Advertisement

# Register your models here.
@admin.register(Advertisement)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'creator', 'created_at', 'updated_at']
    list_filter = ['id', 'title', 'description', 'status', 'creator', 'created_at', 'updated_at']
