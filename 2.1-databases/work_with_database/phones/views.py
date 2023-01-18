from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    order_cases = {
        "min_price": "price",
        "max_price": "-price",
        "name": "name"
    }

    sort = request.GET.get("sort", "name")

    phones = Phone.objects.all().order_by(order_cases[sort])

    template = 'catalog.html'
    context = { "phones": phones }
    return render(request, template, context)

def show_product(request, slug):
    phone_product = Phone.objects.filter(slug=slug)

    phones_list = list(phone_product)

    phone = {
        "name": phones_list[0].name,
        "price": phones_list[0].price,
        "image": phones_list[0].image_url,
        "release_date": phones_list[0].release_date,
        "lte_exist": phones_list[0].lte_exist,
        "slug": phones_list[0].slug
    }

    template = 'product.html'
    context = { "phone": phone }
    print(context)

    return render(request, template, context)
