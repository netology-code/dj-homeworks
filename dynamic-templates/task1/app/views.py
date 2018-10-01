from django.shortcuts import render
from django.views.generic import TemplateView

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        context = {}
        return render(request, self.template_name,
                      context)