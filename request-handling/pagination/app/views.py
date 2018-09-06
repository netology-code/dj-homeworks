from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'current_page': 1,
        'prev_page_url': None,
        'next_page_url': 'bus_stations/?page=2',
    })

