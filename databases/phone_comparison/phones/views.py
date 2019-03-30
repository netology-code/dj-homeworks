from django.shortcuts import render


from phones.models import Phone


def show_catalog(request):

    context = {
        'characteristics': [
            {
                'name': 'phone_model',
                'verbose_name': 'Модель',
                'show': False
            },{
                'name': 'phone_price',
                'verbose_name': 'Цена',
                'show': False
            },{
                'name': 'phone_os',
                'verbose_name': 'Операционная система',
                'show': False
            },{
                'name': 'phone_manufacturer',
                'verbose_name': 'Производитель',
                'show': False
            },{
                'name': 'phone_memory',
                'verbose_name': 'Размер оперативной памяти',
                'show': False
            },{
                'name': 'phone_ppi',
                'verbose_name': 'Число пикселей на дюйм',
                'show': False
            },{
                'name': 'phone_cameras',
                'verbose_name': 'Камера',
                'show': False
            },{
                'name': 'phone_processor',
                'verbose_name': 'Процессор',
                'show': False
            },{
                'name': 'phone_screen_resolution',
                'verbose_name': 'Разрешение экрана',
                'show': False
            },{
                'name': 'phone_fm_radio',
                'verbose_name': 'FM-радио',
                'show': False
            },
            {
                'name': 'phone_addition',
                'verbose_name': 'Дополнительно',
                'show': False
            },
        ]
    }

    phones = Phone.objects.select_related().all()
    context['phones'] = phones

    for characteristic in context['characteristics']:
        for phone in phones:
            try:
                if phone.__getattribute__(characteristic['name']):
                    characteristic['show'] = True
                    break
            except AttributeError:
                pass

    return render(
        request,
        'catalog.html',
        context
    )
