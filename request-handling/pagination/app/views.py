<<<<<<< HEAD
from django.core.paginator import Paginator
=======
>>>>>>> 72652d08d30426b23a1dcc1c0b415b545b92fb8c
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
<<<<<<< HEAD
    with open(settings.BUS_STATION_CSV) as isfile:
        reader = csv.DictReader(isfile, delimiter=',')
        read = list(reader)
=======
    current_page = 1
    next_page_url = 'write your url'
    return render(request, 'index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
                         {'Name': 'другое название', 'Street': 'другая улица', 'District': 'другой район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })
>>>>>>> 72652d08d30426b23a1dcc1c0b415b545b92fb8c

        paginator = Paginator(read, 10)
        current_page = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(current_page)
        data = page_obj.object_list

        prev_page_url, next_page_url = None, None
        if page_obj.has_previous():
            prev_page_url = page_obj.previous_page_number()
        if page_obj.has_next():
            next_page_url = page_obj.next_page_number()

        context = {
            'bus_stations': data,
            'current_page': page_obj.number,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url
        }
        return render(request, 'index.html', context=context)
