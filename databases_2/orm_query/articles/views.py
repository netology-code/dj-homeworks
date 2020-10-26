from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = '-published_at'
    obj_list = Article.objects.select_related('genre', 'author').order_by(ordering)
    context = {'object_list': obj_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template_name, context)
