from django.shortcuts import render


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg', 'original')
    if ab_test_arg == 'test':
        return landing_b(request)
    else:
        return landing_a(request)


def landing_a(request):
    return render(request, 'landing/index.html', context={'ab_test_arg': request.GET.get('ab-test-arg', 'nothing')})


def landing_b(request):
    return render(request, 'landing/index_alternate.html', context={'ab_test_arg': request.GET.get('ab-test-arg', 'nothing')})
