from django.shortcuts import render, get_object_or_404
from pages.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def bicycles(request, pk=None, page=1):
    links_menu = Category.objects.all()
    title = {
        'site': 'ВелоЗапча',
        'page': 'Велики'
        }

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'pages/products_list.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
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


def product(request, pk):
    title = 'Товар из магазина'
    
    context = {
        'title': title, 
        'links_menu': Category.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': get_basket(request.user),
    }
    
    return render(request, 'pages/product.html', context)

