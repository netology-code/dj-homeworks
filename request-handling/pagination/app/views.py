from django.shortcuts import render_to_response, redirect, Http404
from django.urls import reverse

from django.conf import settings
import csv
import urllib


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    try:
        current_page = int(request.GET.get('page', '1'))
    except ValueError:
        current_page = 1

    with open(settings.BUS_STATION_CSV, 'rt', encoding='cp1251') as f:
        reader = csv.DictReader(f)
        bus_stations = []
        for_next_page = False
        try:
            for _ in range((current_page - 1) * 10):
                next(reader)
            for _ in range(10):
                bus_stations.append(next(reader))
            if next(reader):
                for_next_page = True
        except StopIteration:
            pass  

    if not bus_stations:
         raise Http404('Страница не найдена')

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': None if current_page == 1 else '?' + urllib.parse.urlencode({'page': current_page - 1}),
        'next_page_url': '?' + urllib.parse.urlencode({'page': current_page + 1}) if for_next_page else None,
    })

