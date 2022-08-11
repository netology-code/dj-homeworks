from django.contrib import admin

from .models import Article, Teg, ArticleTeg


class ArticleTegInline(admin.TabularInline):
    model = ArticleTeg
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['published_at']
    inlines = [ArticleTegInline, ]


@admin.register(Teg)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
