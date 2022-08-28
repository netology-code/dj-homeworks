from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'stocks']
    list_filter = ['title']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'positions']
    list_filter = ['id', 'address']
    inlines = [StockProductInline, ]


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']
