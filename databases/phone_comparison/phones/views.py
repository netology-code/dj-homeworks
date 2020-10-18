from django.shortcuts import render
from .models import Phone, UniqPhone


def show_catalog(request):
    phones = Phone.objects.all()
    uniq = UniqPhone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones,
               'uniq': uniq}
    return render(
        request,
        template,
        context
    )
