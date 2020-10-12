from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import timezone, dateformat
import os
import json


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    msg = f'Текущее время: {current_time}'

    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = "/"
    dir_list = os.listdir(path)
    list_as_json = json.dumps(dir_list)
    return HttpResponse(list_as_json, content_type="application/json")
