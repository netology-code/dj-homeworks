from django.urls import path

from articles.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view()),
]
