from django.shortcuts import render


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    return render(
        request,
        'signup.html'
    )
