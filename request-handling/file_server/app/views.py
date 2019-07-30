import datetime

from django.shortcuts import render
from app import settings
import os


def convert_date(some_int):
    return datetime.datetime.fromtimestamp(some_int).strftime("%d %B %Y %H:%M")

def unconvert_date(date):
    return datetime.datetime.strptime(' '.join(date.split(' ')[:3]), "%d %B %Y").strftime("%d %m %Y")

def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    file_list = os.listdir(settings.FILES_PATH)
    files = []

    for file in file_list:
        files.append(
            {
                'name' : file,
                'ctime' : convert_date(os.stat(os.path.join(settings.FILES_PATH, file))[9]),
                'mtime' : convert_date(os.stat(os.path.join(settings.FILES_PATH, file))[8])
            }
        )

    if year != None and month != None and day != None:
        search_date = datetime.date(year, month, day).strftime("%d %m %Y")
        searched_file = []
        for file in files:
            if unconvert_date(file['mtime']) == search_date:
                searched_file.append(file)

        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        context = {
            'files': searched_file
        }
        print(context)
        return render(request, template_name, context)

    context = {'files': files['files']}

    return render(request, template_name, context)


def file_content(request, name):
    template_name = 'file_content.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_content = []
    with open(os.path.join(settings.FILES_PATH, name), 'r') as file:
        for line in file:
            file_content.append(line)

    return render(
        request,
        template_name,
        context={'file_name': name, 'file_content': file_content}
    )