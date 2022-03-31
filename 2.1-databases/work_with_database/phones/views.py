from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phones.order_by("name")
    elif sort == 'min_price':
        phones = phones.order_by("price")
    elif sort == 'max_price':
        phones = phones.order_by("-price")

    data = [phone.__dict__ for phone in phones]

    template = 'catalog.html'
    context = {'phones': data}
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=slug)
    # print(phone_objects[0].__dict__)
    template = 'product.html'
    context = {'phone': phone_objects[0].__dict__}
    return render(request, template, context)


def show_db(request):
    phone_objects = Phone.objects.all()
    phones = [f'{p.id}: {p.name}, {p.slug}, {p.image}, {p.price}, {p.release_date}, {p.lte_exists}' for p in
              phone_objects]
    return HttpResponse('<br>'.join(phones))
