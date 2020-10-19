from django.shortcuts import render
from .models import Phone, UniqPhone, PhoneTables
from django_tables2 import RequestConfig


def show_catalog(request):
    phones = Phone.objects.all()
    uniq = PhoneTables(UniqPhone.objects.all())
    RequestConfig(request).configure(uniq)

    names = ["Название", "Стоимость", "Камера"]
    template = 'catalog.html'
    context = {'phones': phones,
               'uniq': uniq,
               'names': names}
    return render(
        request,
        template,
        context
    )
