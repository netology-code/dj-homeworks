import datetime

from django.shortcuts import render, Http404
from django.views.generic import TemplateView

import os
from django.conf import settings

class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        # return {
        #     'files': [
        #         {'name': 'file_name_1.txt',
        #          'ctime': datetime.datetime(2018, 1, 1),
        #          'mtime': datetime.datetime(2018, 1, 2)}
        #     ],
        #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        # }

        res = {
            'files': []
        }

        if date is not None:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            res['date'] = date

        files = os.listdir(settings.FILES_PATH)

        for name in files:

            stat = os.stat(os.path.join(settings.FILES_PATH, name))
            ctime = datetime.datetime.fromtimestamp(stat.st_ctime)
            mtime = datetime.datetime.fromtimestamp(stat.st_mtime)

            if date is None or date in (ctime.date(), mtime.date()):
                res['files'].append({
                    'name': name,
                    'ctime': ctime,
                    'mtime': mtime,
                })

        return res


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # return render(
    #     request,
    #     'file_content.html',
    #     context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
    # )

    try:
        with open(os.path.join(settings.FILES_PATH, name), 'rt', encoding='utf-8') as f:
            file_content = f.read()
    except FileNotFoundError:
        raise Http404()
        
    return render(
        request,
        'file_content.html',
        context={
            'file_name': name,
            'file_content': file_content
        }
    )

