from django.shortcuts import render, get_object_or_404, reverse
from .models import Product, Order, OrderedItems, ShippingDetails
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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

class AddToCart(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'macrameshop/shopping_cart.html'
    success_url = reverse_lazy('macrameshop:products')


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


def add_likes(request, pk):
    liked_product = get_object_or_404(Product, id=pk)
    liked_product.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))

