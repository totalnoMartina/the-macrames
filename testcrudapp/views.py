from django.shortcuts import render, redirect
from .models import Product, Ordering, Customer
from .forms import OrderingForm


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

def create_order(request):

    form = OrderingForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        print('Printing Post:', request.POST)
        form = OrderingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'testcrudapp/order_form.html', context)

def update_order(request, pk):

    order_ = Ordering.objects.get(id=pk)

    form = OrderingForm(instance=order_)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = OrderingForm(request.POST, instance=order_)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'testcrudapp/order_form.html', context)


def delete_order(request, pk):
    order_ = Ordering.objects.get(id=pk)
    form = OrderingForm(instance=order_)

    context = {
        # 'form': form,
        'item': order_,
    }

    if request.method == 'POST':
        order_.delete()
        return redirect('/')

    return render(request, 'testcrudapp/delete.html', context)
