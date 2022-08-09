from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': list(Book.objects.all())}
    return render(request, template, context)


def books_paginator(request, pub_date):
    template = 'books/books_pagi.html'
    books_object = Book.objects.all().order_by('pub_date')
    dates = [str(book_date) for book_dates in books_object.values('pub_date') for book_date in book_dates.values()]
    pub_date_index = dates.index(pub_date)
    print(dates[pub_date_index])
    paginator = Paginator(dates, 1)
    page = paginator.get_page(dates.index(pub_date) + 1)
    if pub_date_index < len(dates) - 1:
        next_page = dates[pub_date_index + 1]
    else:
        next_page = None
    if pub_date_index > 0:
        previous_page = dates[pub_date_index - 1]
    else:
        previous_page = None
    context = {'page': page,
               'previous_page': previous_page,
               'next_page': next_page,
               'books': list(Book.objects.filter(pub_date=pub_date)),
               'pub_date': pub_date}
    return render(request, template, context)
