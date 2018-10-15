from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
