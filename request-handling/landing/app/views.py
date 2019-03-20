from collections import Counter

from django.shortcuts import render_to_response, Http404

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.method == 'GET':
        ab_test_arg = request.GET.get('from-landing', '')
        if ab_test_arg in ['original', 'test']:
            counter_click[ab_test_arg] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    if request.method == 'GET':
        ab_test_arg = request.GET.get('ab-test-arg', 'original')
        if ab_test_arg == 'test':
            counter_show['test'] += 1
            return render_to_response('landing_alternate.html')
        elif ab_test_arg and ab_test_arg != 'original':
            raise Http404('Нет такой страницы')
    counter_show['original'] += 1
    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': 0 if not counter_show['test'] else counter_click['test'] / counter_show['test'],
        'original_conversion': 0 if not counter_show['original'] else counter_click['original'] / counter_show['original'],
    })
