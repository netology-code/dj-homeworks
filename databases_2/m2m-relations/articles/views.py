from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScope, Scope


def articles_list(request):
    template = 'articles/news.html'
    scope = Article.objects.prefetch_related('art_name', 'name_scope').all()
    context = {'object_list': scope}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
