from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Ordering, Customer


def home(request):
    """ To render items in Dashboard - homepage """
    orders = Ordering.objects.all()
    customers = Customer.objects.all()

    context = {
        'ordering': orders,
        'customers': customers
    }
    return render(request, 'testcrudapp/dashboard.html', context)



def products(request):

    product_items = Product.objects.all()
    return render(request, 'testcrudapp/products.html', {'product_items': product_items})