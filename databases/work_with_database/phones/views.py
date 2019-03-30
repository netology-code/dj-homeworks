from django.shortcuts import render, get_object_or_404
from phones.models import Phone


def show_catalog(request):

    order_by = request.GET.get('order_by', None)

    if order_by is not None and order_by in ['name', '-name', 'price', '-price']:
        phones = Phone.objects.all().order_by(order_by)
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):

    phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone': phone
    }

    return render(
        request,
        'product.html',
        context
    )
