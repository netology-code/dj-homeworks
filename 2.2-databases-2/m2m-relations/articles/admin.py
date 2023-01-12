from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Teg, ArticleTeg


class ArticleTegInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_teg_list = []
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data:
                main_teg_list.append(form.cleaned_data['main_teg'])
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if not any(main_teg_list):
            raise ValidationError('Укажите основной раздел')
        if sum(main_teg_list) > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTegInline(admin.TabularInline):
    model = ArticleTeg
    extra = 1
    formset = ArticleTegInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['published_at']
    inlines = [ArticleTegInline, ]


@admin.register(Teg)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
