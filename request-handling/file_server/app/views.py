import datetime

from django.shortcuts import render
from app import settings
import os


def file_list(request):
    template_name = 'index.html'
    
    file_list = os.listdir(settings.FILES_PATH)
    files = []

    for file in file_list:
        files.append(
            {
                'name' : file,
                'ctime' : datetime.datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file))[9]).strftime("%d %B %Y %H:%M"),
                'mtime' : datetime.datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file))[8]).strftime("%d %B %Y %H:%M")
            }
        )

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files,
        'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_list = os.listdir(settings.FILES_PATH)

    return render(
        request,
        'file_content.html',
        context={'file_name': 'server.01', 'file_content': 'File content!'}
    )


