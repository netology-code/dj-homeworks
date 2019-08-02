from django.urls import path
from app.views import file_list, file_content

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    path('file/<str:name>/', file_content, name='file_content'),
    path('<int:year>-<int:month>-<int:day>/', file_list, name='file_list_filtered'),
    path('', file_list, name='file_list')
]