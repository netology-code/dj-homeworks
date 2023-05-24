
import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

STATIONS = []
with open(settings.BUS_STATION_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        STATIONS.append({"Name": row["Name"], "Street": row["Street"], "District": row["District"]})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(STATIONS, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
