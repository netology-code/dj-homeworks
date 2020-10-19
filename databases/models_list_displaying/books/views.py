from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def book_view(request, date):

    book = Book.objects.all()
    paginator = Paginator(book, 1)
    current_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(current_page)
    data = page_obj.object_list

    prev_page_url, next_page_url = None, None
    if page_obj.has_previous():
        prev_page_url = page_obj.previous_page_number()
    if page_obj.has_next():
        next_page_url = page_obj.next_page_number()
    template = 'books/book.html'
    context = {
        'book': data,
        'current_page': page_obj.number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url
    }
    return render(request, template, context)
