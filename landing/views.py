from collections import Counter

from django.shortcuts import render_to_response

# Для отладки миханизма используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что на самом деле так не стоит делать
# и при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def landing(request):
    # Реализуйте дополнительное отображение по шаблону landing/index_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    return render_to_response('landing/index.html')
# TODO: remove solution
#     ab_test_arg = request.GET.get('ab-test-arg', 'original')
#     if ab_test_arg == 'test':
#         return landing_b(request)
#     else:
#         return landing_a(request)
#
#
# def landing_a(request):
#     counter_show['original'] += 1
#     return render_to_response('landing/index.html')
#
#
# def landing_b(request):
#     counter_show['test'] += 1
#     return render_to_response('landing/index_alternate.html')


def stats(request):
    # Реализуйте логику подсчета количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    return render_to_response('landing/stats.html', context={
        'test_conversion': 0.5,
        'original_conversion': 0.4,
    })
    # if 'marker' in request.GET:
    #     counter_click[request.GET['marker']] += 1
    # return render_to_response('landing/stats.html', context={
    #     'test_conversion': counter_show['test'] and counter_click['test'] / counter_show['test'],
    #     'original_conversion': counter_show['original'] and counter_click['original'] / counter_show['original'],
    # })
