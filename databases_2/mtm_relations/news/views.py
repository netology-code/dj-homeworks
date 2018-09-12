from django.shortcuts import render, redirect
from .models import Section, Article, SectionMember
from .forms import ArticleForm, SectionMemberForm
from django.views.generic import TemplateView


def index(request, *args, **kwargs):
    if "section_id" in kwargs:
        sec_members = SectionMember.objects.filter(section__id=kwargs["section_id"])
        articles = [sm.article for sm in sec_members]
    else:
        articles = Article.objects.all()

    data = {"sections": Section.objects.all(), "articles": articles}
    return render(request, 'news/news_list.html', context=data)


class ArticleCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = {"form": ArticleForm(sections=Section.objects.all())}
        return render(request, 'news/news_create.html', context=data)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            pub_date = form.cleaned_data['pub_date']
            additional_sections = form.cleaned_data['additional_sections']
            main_section = form.cleaned_data['main_section']
            image = form.cleaned_data['image']

            article = Article(title=title, text=text, pub_date=pub_date, image=image)
            article.save()

            for sec in main_section:
                sec_member = SectionMember(section=Section.objects.get(pk=sec), main=True, article=article)
                sec_member.save()

            for sec in additional_sections:
                sec_member = SectionMember(section=Section.objects.get(pk=sec), main=False, article=article)
                sec_member.save()

            return redirect("home")


class SectionMemberCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = {"form": SectionMemberForm(articles=Article.objects.all(), sections=Section.objects.all())}
        return render(request, 'news/section_member_add.html', context=data)

    def post(self, request, *args, **kwargs):
        form = SectionMemberForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.cleaned_data['article']
            main = form.cleaned_data['main']
            section = form.cleaned_data['section']

            sec_member = SectionMember(article=Article.objects.get(pk=article), main=main,
                                       section=Section.objects.get(pk=section))
            sec_member.save()

            return redirect("home")
