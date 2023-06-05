
from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    if request.GET.get("sort") == "name":
        phones = phones.order_by("name")
    elif request.GET.get("sort") == "min_price":
        phones = phones.order_by("name").order_by("price")
    elif request.GET.get("sort") == "max_price":
        phones = phones.order_by("name").order_by("-price")

    context = {"phones": []}
    for ph in phones:
        context["phones"].append({
            "name": ph.name,
            "image": ph.image,
            "price": ph.price,
            "slug": ph.slug
        })
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    ph = Phone.objects.get(slug=slug)
    context = {
        "phone": {
            "name": ph.name,
            "image": ph.image,
            "price": ph.price,
            "release_date": ph.release_date,
            "lte_exists": ph.lte_exists,
        }
    }
    return render(request, template, context)
