import datetime

from django.urls import path, register_converter

from file_server.views import FileList, file

class Date:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.datetime.strptime(value, self.format).date()

    def to_url(self, value: datetime.datetime):
        return value.strftime(self.format)


register_converter(Date, 'date')


urlpatterns = [
    path('', FileList.as_view(), name='index'),
    path('<date:date>', FileList.as_view(), name='index'),
    path('file/<name>', file, name='file'),
]
