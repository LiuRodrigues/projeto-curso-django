from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html',)


def land(request):
    return render(request, 'recipes/pages/land-page.html',)
