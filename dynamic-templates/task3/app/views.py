import requests
from django.shortcuts import render


def do_request():
    resp = requests.get('https://reddit.com/r/Python/top.json',
                        headers={'User-Agent': 'Python Netology'})
    return resp.json()['data']['children']


def convert_post(post):
    yield post


def top_reddit_view(request):
    template_name = 'top_reddit.html'

    posts = do_request()
    context = {
        'posts': posts,
        'prefix': 'https://reddit.com'
    }
    return render(request, template_name, context)
