from django.shortcuts import render, get_object_or_404
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        return render(request, template, {'all_phones': all_phones.order_by('name')})
    if request.GET.get('sort') == 'min_price':
        return render(request, template, {'all_phones': all_phones.order_by('price')})
    if request.GET.get('sort') == 'max_price':
        return render(request, template, {'all_phones': all_phones.order_by('-price')})
    return render(request, template, {'all_phones': all_phones})


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, template, {'phone': phone})
