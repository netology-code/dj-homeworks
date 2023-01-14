from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    class Station:
        def __init__(self, name, street, district):
            self.Name = name
            self.Street = street
            self.District = district

    bus_stations = []

    with open("data-398-2018-08-30.csv", newline="") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append(
                Station(name=row["Name"], 
                    street=row["Street"],
                    district=row["District"]))

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 5)
    page = paginator.get_page(page_number)

    print(page)

    context = {
         #'bus_stations': paginator,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
