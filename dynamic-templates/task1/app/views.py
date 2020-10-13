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
                rows.append(row)

        for r in rows:
            for i, val in enumerate(r[1:]):

                if '.' in val or r[i] is not None:
                    r[i] = float(r[i])

                #if val == '':
                 #   r[i] = '-'
                #if 1 < int(val) < 2:
                 #   r[i].style


    # чтение csv-файла и заполнение контекста
    context = {'data': rows, 'header': header}

    return render(request, template_name,
                  context=context)
