from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV) as isfile:
        reader = csv.DictReader(isfile, delimiter=',')
        read = list(reader)

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
