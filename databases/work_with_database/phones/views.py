from django.shortcuts import render


def show_catalog(request):
    return render(
        request,
        'catalog.html',
    )


def show_product(request, slug):
    return render(
        request,
        'product.html',
    )
