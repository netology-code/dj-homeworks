import requests
from django.shortcuts import render
from django.views.generic import TemplateView


def do_request():
    resp = requests.get('https://reddit.com/r/Python/top.json',
                        headers={'User-Agent': 'Python Netology'})
    return resp.json()['data']['children']


def convert_post(post):
    yield post


class TopRedditView(TemplateView):
    template_name = 'top_reddit.html'

    def get(self, request, *args, **kwargs):
        posts = do_request()
        context = {
            'posts': posts,
            'prefix': 'https://reddit.com'
        }
        return render(request, self.template_name,
                      context)
