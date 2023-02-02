from django.contrib import admin

from .models import Article, Tag, ArticleTag

class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['title', 'published_at']
    inlines = [ArticleTagInline, ]

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    inlines = [ArticleTagInline, ]

