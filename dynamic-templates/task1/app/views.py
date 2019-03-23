from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings
import csv

class InflationView(TemplateView):

    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):

        # чтение csv-файла и заполнение контекста

        context = {}

        with open(settings.DATA_FILE, 'rt', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            context['inflation_data'] = [data_row for data_row in reader]
        
        return render(request, self.template_name, context)