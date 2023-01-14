class Station:
    def __init__(self, name, street, district) -> None:
        self.Name = name
        self.Street = street
        self.District = district


import csv
from urllib import request
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

bus_stations = []

with open("data-398-2018-08-30.csv", newline="") as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        bus_stations.append(
            Station(name=row["Name"], 
                    street=row["Street"],
                    district=row["District"]))

page_number = 1 #int(request.GET.get("page", 1))
paginator = Paginator(bus_stations, 5)
page = paginator.get_page(page_number)

print(page)
