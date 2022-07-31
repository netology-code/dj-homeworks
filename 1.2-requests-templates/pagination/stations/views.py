from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

import pagination.settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(pagination.settings.BUS_STATION_CSV, encoding='utf8') as csvfile:
        reader = list(csv.DictReader(csvfile))
    paginator = Paginator(reader, 10)
    page = paginator.get_page(page_number)
    context = {'page': page,
              }
    return render(request, 'stations/index.html', context)
