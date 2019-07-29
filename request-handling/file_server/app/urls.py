from django.urls import path
from app.views import file_list, file_content

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    path('', file_list, name='file_list'),
    path('<int:arg1>/<int:arg2>/<int:arg3>/', file_list, name='file_list'),
    path('file/<str:file_name>/', file_content, name='file_content')
]
