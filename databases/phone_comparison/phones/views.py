from django.shortcuts import render


def show_catalog(request):
    return render(
        request,
        'catalog.html'
    )
