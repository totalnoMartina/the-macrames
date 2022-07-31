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
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, completed_order=False)
        items = order.ordereditems_set.all()
    else:
        items = []
        order = { 'get_cart_tot': 0, 'get_cart_items': 0}
    context = {
        'items': items, 'order': order
    }
    return render(request, 'macrameshop/shopping_cart.html', context)


def checkout(request):
    """ A view to display shopping cart """
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, completed_order=False)
        items = order.ordereditems_set.all()
    else:
        items = []
        order = { 'get_cart_tot': 0, 'get_cart_items': 0}
    context = {
        'items': items, 'order': order
    }

    return render(request, 'macrameshop/checkout.html', context)