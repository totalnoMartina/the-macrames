from django.shortcuts import render
from .models import Product, Ordering, Customer


def home(request):
    """ To render items in Dashboard - homepage """
    ordering = Ordering.objects.all()
    customers = Customer.objects.all()
    customers_total = customers.count()
    total_orders = ordering.count()
    delivered_o = ordering.filter(status='Delivered').count()
    pending_o = ordering.filter(status='Pending').count()

    context = {
        'ordering': ordering,
        'customers': customers,
        'total_orders': total_orders,
        'delivered_o': delivered_o,
        'pending_o': pending_o,
    }
    return render(request, 'testcrudapp/dashboard.html', context)


def products(request):

    product_ = Product.objects.all()
    context = {
        'product_': product_,

    }
    return render(request, 'testcrudapp/products.html', context)


def customer(request, pk):
    customer_ = Customer.objects.get(id=pk)
    ordering = customer_.ordering_set.all()
    order_count = ordering.count()
    context = {
        'customer_': customer_,
        'ordering': ordering,
        'order_count': order_count,
    }

    return render(request, 'testcrudapp/customer.html', context)
