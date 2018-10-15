from django.views import generic


class BookListView(generic.ListView):
    def get_context_data(self, **kwargs):
        pass
