from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.all()
    template = 'articles/news.html'

    context = {'object_list': articles}
    print(context)
    for article in articles:
        print(article.title, ":")
        for scope in article.scopes.all():
            print(scope.is_main, scope.tag.name)


    return render(request, template, context)
