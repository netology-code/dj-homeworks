import datetime

from django.shortcuts import render


def file_list(request):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': [
            {'name': 'file_name_1.txt',
             'ctime': datetime.datetime(2018, 1, 1),
             'mtime': datetime.datetime(2018, 1, 2)}
        ],
        'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
    )

