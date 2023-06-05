
from datetime import datetime

from django.shortcuts import render

from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {"books": []}
    for b in books:
        cur_date = b.pub_date.strftime("%Y-%m-%d")
        context["books"].append({
            "name": b.name,
            "author": b.author,
            "pub_date": cur_date
        })
    return render(request, template, context)

def date_view(request, pub_date):
    template = 'books/date_view.html'
    books = Book.objects.all().order_by("pub_date")
    context = {"date": pub_date, "books": [],
               "prev_date": None, "next_date": None }
    if len(books):
        for b in books:
            cur_date = b.pub_date.strftime("%Y-%m-%d")
            if cur_date < pub_date:
                context["prev_date"] = cur_date
            if cur_date == pub_date:
                context["books"].append({
                    "name": b.name,
                    "author": b.author,
                    "pub_date": cur_date
                })
            if not context["next_date"] and cur_date > pub_date:
                context["next_date"] = cur_date
    return render(request, template, context)
