from django.shortcuts import render
import csv
import io


def inflation_view(request):
    template_name = 'inflation.html'
    rows = []

    with io.open('inflation_russia.csv', encoding='utf-8') as isfile:
        file = csv.reader(isfile, delimiter=';')
        linecount = 0
        for row in file:
            if linecount == 0:
                header = row
                linecount += 1
            else:
                converted_data = [row[0]]
                for i in row[1:]:
                    try:
                        converted_data.append(float(i))
                    except:
                        converted_data.append('-')
                rows.append(converted_data)

    # чтение csv-файла и заполнение контекста
    context = {'data': rows, 'header': header}

    return render(request, template_name,
                  context=context)
