from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

