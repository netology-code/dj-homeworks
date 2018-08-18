import datetime
import os
from collections import namedtuple

from django.conf import settings
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


FileData = namedtuple('FileData', 'name,path,ctime,mtime')


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # TODO: убрать решение:
        # data = super().get_context_data()
        # dir_content = [os.path.join(settings.FILES_PATH, f)
        #                for f in os.listdir(settings.FILES_PATH)]
        # files = []
        # for path in dir_content:
        #     if os.path.isfile(path):
        #         st = os.stat(path)
        #         ctime = datetime.datetime.fromtimestamp(st.st_ctime)
        #         mtime = datetime.datetime.fromtimestamp(st.st_mtime)
        #         if date and date not in (ctime.date(), mtime.date()):
        #             continue
        #         files.append(FileData(
        #             os.path.basename(path),
        #             path,
        #             ctime,
        #             mtime,
        #         ))
        # data['files'] = sorted(files)
        # data['date'] = date
        # return data

        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return {
            'files': [
                {'name': 'file_name_1.txt',
                 'ctime': datetime.datetime(2018, 1, 1),
                 'mtime': datetime.datetime(2018, 1, 2)}
            ],
            'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }


def file_content(request, name):
    # TODO: убрать решение:
    # with open(os.path.join(os.path.join(settings.FILES_PATH, name)), 'r') as f:
    #     return render_to_response('file_content.html', context=dict(file_name=name, file_content=f.read()))

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render_to_response(
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
    )

