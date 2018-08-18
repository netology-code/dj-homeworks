import datetime

from django.urls import path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

# TODO: убрать решение:
# from django.urls import register_converter
# from app.views import FileList, file_content
#
# class Date:
#     regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
#     format = '%Y-%m-%d'
#
#     def to_python(self, value):
#         return datetime.datetime.strptime(value, self.format).date()
#
#     def to_url(self, value: datetime.datetime):
#         return value.strftime(self.format)
#
#
# register_converter(Date, 'date')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content

    # TODO: убрать решение:
    # path('', FileList.as_view(), name='file_list'),
    # path('<date:date>', FileList.as_view(), name='file_list'),
    # path('file/<name>', file_content, name='file_content'),
]
