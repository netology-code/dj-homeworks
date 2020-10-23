from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(RelationshipInlineFormset, self).clean()
        main_check = 0

        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and form.cleaned_data.get('DELETE'):
                if form.cleaned_data['is_main']:
                    main_check += 1

        if main_check > 1:
            raise ValidationError('Основным может быть только один раздел')

        if main_check < 1:
            raise ValidationError('Укажите основной раздел')


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(ArticleScope)
class ObjectAdmin(admin.ModelAdmin):
    pass
