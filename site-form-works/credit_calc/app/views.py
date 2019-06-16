from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm
    context = {
        'form': form
    }

    return render(request, template, context)
