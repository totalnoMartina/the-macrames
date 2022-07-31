from django.shortcuts import render
from .models import *


def index(request):
    """ A view to display homepage """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'macrameshop/index.html', context)


def shopping_cart(request):
    """ A view to display shopping cart """
    context = {}
    return render(request, 'macrameshop/shopping_cart.html', context)


def checkout(request):
    """ A view to display shopping cart """
    context = {}

    return render(request, 'macrameshop/checkout.html', context)