from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', None)
    if sort == 'name':
        phones = list(Phone.objects.all().order_by(sort))
    elif sort == 'min_price':
        phones = list(Phone.objects.all().order_by('price'))
    elif sort == 'max_price':
        phones = list(Phone.objects.all().order_by('-price'))
    else:
        phones = list(Phone.objects.all())
    print(phones)
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    print(context['phone'])
    return render(request, template, context)
