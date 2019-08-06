from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    file_path = r'inflation_russia.csv'

    values = []

    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames[0].split(';')
        for line in reader:
            for value in line.values():
                values.append(value.split(';'))

    for i, value in enumerate(values):
        for num, row in enumerate(value):
            try:
                if num == 0:
                    value[num] = str(row)
                else:
                    value[num] = float(row)
            except ValueError:
                value[num] = row

    # чтение csv-файла и заполнение контекста

    context = {
        'headers' : headers,
        'values' : values}

    return render(request, template_name,
                  context=context)





'''values = []

with open(file_path, encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    headers = reader.fieldnames[0].split(';')
    for line in reader:
        for value in line.values():
            values.append(value.split(';'))

for i, value in enumerate(values):
    for num, row in enumerate(value):
        try:
            if num == 0:
                value[num] = str(row)
            else:
                value[num] = float(row)
        except ValueError:
            value[num] = row'''