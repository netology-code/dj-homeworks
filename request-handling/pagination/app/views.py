import csv
from app import settings
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import urllib.parse as urllib
from django.core.paginator import Paginator


def read_file(file_path=settings.BUS_STATION_CSV):
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
    query = {"page": [page]}
    link = reverse('bus_stations') + '?' + urllib.urlencode(query, doseq=True)

    print(link)

    try:
        prev_page_num = paginator.get_page(page).previous_page_number()
    except:
        prev_page_num = 1
    next_page_num = paginator.get_page(page).next_page_number()

    try:
        if paginator.get_page(page).has_previous():
            prev_page = reverse('bus_stations') + '?page=' + str(prev_page_num)
        else:
            page = 1
            prev_page = ''

        if paginator.get_page(page).has_next():
            next_page = reverse('bus_stations') + '?page=' + str(next_page_num)
        else:
            next_page = reverse('bus_stations')
    except TypeError:
        page = 1
        next_page = reverse('bus_stations') + '?page=2'
        prev_page = ''

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': page,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    })
