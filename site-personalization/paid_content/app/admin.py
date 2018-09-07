from django.contrib import admin

from app.models import Profile, Article


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid",)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pay',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article, ArticleAdmin)
