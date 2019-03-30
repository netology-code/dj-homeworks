import datetime

from django.views import generic
from django.shortcuts import Http404, get_object_or_404

from books.models import Book


class BookListView(generic.ListView):

    model = Book
    template_name = 'books/book_list.html'
    context_object_name = "books"

    def get_context_data(self, **kwargs):

        date = self.request.resolver_match.kwargs.get('date')
        if date is not None:
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                try:
                    previous_book = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').get().pub_date
                except Book.DoesNotExist:
                    previous_book = None
                try:
                    next_book = Book.objects.filter(pub_date__gt=date).order_by('pub_date').get().pub_date
                except Book.DoesNotExist:
                    next_book = None
                return {
                    'books': [get_object_or_404(Book, pub_date=date)],
                    'page_obj': {
                        'previous': previous_book,
                        'next': next_book
                    }
                }
            except:
                raise Http404

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Book.objects.order_by('pub_date').all()
