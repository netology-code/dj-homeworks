from django.shortcuts import render

from app.models import Article


def show_articles(request):
    articles = Article.objects.all()

    return render(
        request,
        'articles.html',
        {
            'articles': articles
        }
    )


def show_article(request, id):
    article = Article.objects.get(id=id)
    is_paid = request.user.profile.is_paid

    return render(
        request,
        'article.html',
        {
            'article': article,
            'is_paid': is_paid
        }
    )
