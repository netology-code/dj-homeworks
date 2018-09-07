from django.shortcuts import render

from app.models import Phone


def show_catalog(request):
    parse_csv()

    if request.GET.__len__() != 0:
        if request.GET['order'] == 'name':
            phones = Phone.objects.filter().order_by('name')
        elif request.GET['order'] == 'min_price':
            phones = Phone.objects.filter().order_by('price')
        elif request.GET['order'] == 'max_price':
            phones = Phone.objects.filter().order_by('-price')
        else:
            phones = Phone.objects.all()
    else:
        phones = Phone.objects.all()

    return render(
        request,
        'catalog.html',
        {
            'phones': phones,
        }
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)

    return render(
        request,
        'product.html',
        {
            'phone': phone,
        }
    )


def parse_csv():
    file = open('phones.csv', 'r')

    for index, line in enumerate(file):
        if index == 0:
            continue

        line = line.split(';')
        phone = Phone()
        phone.id = line[0]
        phone.name = line[1]
        phone.image = line[2]
        phone.price = line[3]
        phone.save()

    file.close()
