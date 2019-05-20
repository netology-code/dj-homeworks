from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}

    return render(request, template_name,
                  context)