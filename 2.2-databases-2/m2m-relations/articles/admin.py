from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Tag, Article, Scope


admin.site.register(Tag)


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        form_not_del = [f for f in self.forms if not f.cleaned_data['DELETE']]
        tag_ids = set(form.cleaned_data['tag'].id for form in form_not_del)
        if len(tag_ids) != len(form_not_del):
            raise ValidationError('Найдены дубликаты разделов!')

        is_mains = [form.cleaned_data['is_main'] for form in form_not_del if form.cleaned_data['is_main']]
        print(is_mains)
        if len(is_mains) == 0:
            raise ValidationError('Укажите основной раздел!')

        if len(is_mains) > 1:
            raise ValidationError('Основным может быть только один раздел!')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
