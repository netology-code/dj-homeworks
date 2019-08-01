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

    try:
        next_page = 'bus_stations?page=' + str(int(page) + 1)
        prev_page = 'bus_stations?page=' + str(int(page) - 1)
    except TypeError:
        page = '1'
        next_page = 'bus_stations?page=2'
        prev_page = ''
    except ValueError:
        page = '1'
        next_page = 'bus_stations?page=2'
        prev_page = ''

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': page,
        'prev_page_url': '',
        'next_page_url': next_page
    })
