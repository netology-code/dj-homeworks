
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_exists = False
        for form in self.forms:
            if form.cleaned_data["is_main"]:
                if not main_exists:
                    main_exists = True
                else:
                    raise ValidationError("Только один тэг может быть основным!")
        if not main_exists:
            raise ValidationError("Один из тегов должен быть основным!")
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]