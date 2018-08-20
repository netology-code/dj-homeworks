from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app/home.html'


class AboutView(TemplateView):
    template_name = 'app/about.html'


class ContactsView(TemplateView):
    template_name = 'app/contacts.html'


class ExamplesView(TemplateView):
    template_name = 'app/examples.html'

    def get(self, request, *args, **kwargs):
        items = [{
            'title': 'Apple II',
            'text': 'Легенда',
            'img': 'ii.jpg'
        }, {
            'title': 'Macintosh',
            'text': 'Свежие новинки октября 1983-го',
            'img': 'mac.jpg'
        }, {
            'title': 'iMac',
            'text': 'Оригинальный и прозрачный',
            'img': 'imac.jpg'
        }]
        context = {
            'items': items
        }
        return render(request, self.template_name,
                      context)
