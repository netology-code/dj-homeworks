from django.shortcuts import render


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(
        request,
        template,
        context
    )
