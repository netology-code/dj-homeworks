import csv
from app import settings
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import urllib.parse as urllib
from django.core.paginator import Paginator


def read_file(file_path=settings.BUS_STATION_CSV, encoding='cp1251'):
    bus_stations = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append(
                {
                    'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
                }
            )

    return bus_stations


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    bus_stations_list = read_file()
    paginator = Paginator(bus_stations_list, 10)
    page = request.GET.get('page')
    bus_stations = paginator.get_page(page)
    
    current_page = paginator.get_page(page)

    if current_page.has_next():
        query = {"page": [current_page.next_page_number()]}
        next_page = reverse('bus_stations') + '?' + urllib.urlencode(query, doseq=True)
    else:
        query = {"page": [paginator.num_pages]}
        next_page = reverse('bus_stations') + '?' + urllib.urlencode(query, doseq=True)

    if current_page.has_previous():
        query = {"page": [current_page.previous_page_number()]}
        prev_page = reverse('bus_stations') + '?' + urllib.urlencode(query, doseq=True)
    else:
        page = 1
        prev_page = ''

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': page,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    })
