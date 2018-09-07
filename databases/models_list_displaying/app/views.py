import datetime
from builtins import super

from django.views import generic

from app.models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        if self.kwargs.__len__() > 0:
            pub_date_arr = self.kwargs['pub_date'].split('-')
            return Book.objects.filter(
                pub_date=datetime.date(int(pub_date_arr[0]), int(pub_date_arr[1]), int(pub_date_arr[2])))
        else:
            return Book.objects.filter().order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        if self.kwargs.__len__() > 0:
            pub_date_arr = self.kwargs['pub_date'].split('-')
            book = Book.objects.filter(
                pub_date=datetime.date(int(pub_date_arr[0]), int(pub_date_arr[1]), int(pub_date_arr[2]))).first()

            prev_book = Book.objects.filter(pub_date__lt=book.pub_date).order_by('-pub_date').first()
            next_book = Book.objects.filter(pub_date__gt=book.pub_date).order_by('pub_date').first()
            if prev_book:
                context['prev_date'] = prev_book.pub_date.__str__()
            if next_book:
                context['next_date'] = next_book.pub_date.__str__()
        return context
