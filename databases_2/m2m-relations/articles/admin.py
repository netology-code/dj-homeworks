from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(RelationshipInlineFormset, self).clean()
        main = []
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue

            main.append(form.cleaned_data['is_main'])

        if main.count(True) < 1:
            raise ValidationError('<1')
        elif main.count(True) > 1:
            raise ValidationError('>1')
        else:
            return


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0
    ordering = ("-is_main",)


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(ArticleScope)
class ObjectAdmin(admin.ModelAdmin):
    pass
