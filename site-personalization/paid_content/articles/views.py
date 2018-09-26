from django.shortcuts import render


def show_articles(request):
    return render(
        request,
        'articles.html'
    )


def show_article(request, id):
    return render(
        request,
        'article.html'
    )
