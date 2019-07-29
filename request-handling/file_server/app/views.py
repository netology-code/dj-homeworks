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
    file_content = []

    for file in file_list:
        with open(os.path.join(settings.FILES_PATH, file), 'r') as f:
            file_content.append(
                {
                    'name' : file,
                    'file_content' : f.read()

                }
            )
    return render(
        request,
        'file_content.html',
        context={'file_name': 'server.01', 'file_content': 'File content!'}
    )



import os
fp = r'C:\Users\54292\Desktop\My folder\Python\Netology\dj-homeworks\request-handling\file_server\files'
file_list = os.listdir(r'C:\Users\54292\Desktop\My folder\Python\Netology\dj-homeworks\request-handling\file_server\files')
file_content = []

name = 'server.03'

for file in file_list:
    if name == file:
        with open(os.path.join(fp, file), 'r') as file_content:
            print(file_content.read())