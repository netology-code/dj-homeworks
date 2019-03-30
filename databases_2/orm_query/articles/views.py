from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_queryset(self):
        return Article.objects.defer('published_at', 'author__phone').select_related('author', 'genre').all()