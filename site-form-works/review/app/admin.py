from django.contrib import admin

from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
