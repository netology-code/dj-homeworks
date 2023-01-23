from datetime import datetime
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books_view_my(request, public_date: datetime):
    books_QuerySet = Book.objects.filter(pub_date=public_date)

    books_prev_QuerySet = Book.objects.filter(pub_date__lt=public_date).order_by('-pub_date')[:1]
    public_date_prev_str = get_public_date_str(books_prev_QuerySet)

    books_next_QuerySet = Book.objects.filter(pub_date__gt=public_date).order_by('pub_date')[:1]
    public_date_next_str = get_public_date_str(books_next_QuerySet)
        
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(books_QuerySet, 2)
    page = paginator.get_page(page_number)
    
    template = 'books/books_list_my.html'
    context = {'books': books_QuerySet,
                "page": page,
                "forward_button_title": "ВперЁд",
                "back_button_title": "Назад",
                'public_date_prev_str': public_date_prev_str,
                'public_date_next_str': public_date_next_str
                }
    return render(request, template, context)

def get_public_date_str(book_QuerySet) -> str:
    if book_QuerySet.exists():
        public_date = book_QuerySet[0].pub_date
        public_date_str = public_date.strftime('%Y-%m-%d')    
    else:
        public_date_str = ""
    
    return public_date_str
