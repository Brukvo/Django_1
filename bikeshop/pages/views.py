from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def bicycles(request):
    return render(request, 'pages/bicycles.html')


def not_found(request):
    return render(request, 'pages/404.html')


def parts(request):
    return render(request, 'pages/parts.html')


def accessories(request):
    return render(request, 'pages/accessories.html')


def cart(request):
    return render(request, 'pages/cart.html')


def single(request):
    return render(request, 'pages/single.html')
