from django.shortcuts import render
from pages.models import Product, Category

# Create your views here.
def index(request):
    title = {
        'site': 'ВелоЗапча',
        'page': 'Главная'
        }
    categories = Category.objects.all()

    context = {
        'title': title,
        'categories': categories
        }
    return render(request, 'pages/index.html', context)


def bicycles(request):
    title = {
        'site': 'ВелоЗапча',
        'page': 'Велики'
        }
    context = {
        'title': title
        }
    return render(request, 'pages/bicycles.html', context)


def not_found(request):
    title = {
        'site': 'ВелоЗапча',
        'page': '404'
        }
    context = {
        'title': title
        }
    return render(request, 'pages/404.html', context)


def parts(request):
    title = {
        'site': 'ВелоЗапча',
        'page': 'Запчасти'
        }
    context = {
        'title': title
        }
    return render(request, 'pages/parts.html', context)


def accessories(request):
    title = {
        'site': 'ВелоЗапча',
        'page': 'Аксессуары'
        }
    context = {
        'title': title
        }
    return render(request, 'pages/accessories.html', context)


def cart(request):
    title = {
        'site': 'ВелоЗапча',
        'page': 'Корзина'
        }
    context = {
        'title': title
        }
    return render(request, 'pages/cart.html', context)


def single(request):
    product = Product.objects.all()[3]
    title = {
        'site': 'ВелоЗапча',
        'page': f'{product.name} // {product.category.name}'
        }
    context = {
        'title': title,
        'product': product
        }
    return render(request, 'pages/single.html', context)

