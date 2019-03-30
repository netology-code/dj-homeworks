from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        main_quantity = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main'] and not form.cleaned_data['DELETE']:
                    main_quantity += 1
        if main_quantity > 1:
            raise ValidationError('Должен быть только один основной раздел')
        elif main_quantity == 0:
            raise ValidationError('Должен быть хотя бы один основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = ArticleScopeInlineFormset


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]