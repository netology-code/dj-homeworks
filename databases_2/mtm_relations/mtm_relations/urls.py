"""mtm_relations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from news.views import index, ArticleCreateView, SectionMemberCreateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', index, name="home"),
    url('^article/$', ArticleCreateView.as_view(), name="article"),
    url('^articles/(?P<article_id>\d+)/$', ArticleCreateView.as_view(), name="articles"),
    url('^sections/(?P<section_id>\d+)/$', index, name="sections"),
    url('^section_member/$', SectionMemberCreateView.as_view(), name="section_member_create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
