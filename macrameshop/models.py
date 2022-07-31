from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    """ A class for a buyer profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=150, null=True)

    def __str__(self):
        """ A helper method to see the name of the buyer """
        return self.name


class Product(models.Model):
    """ A class for a product model """
    product = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=900)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ A helper method to see the name of the product """
        return self.product


class Order(models.Model):
    """ A model for an order """
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    ordered = models.DateTimeField(auto_now_add=True)
    completed_order = models.BooleanField(default=False, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        """ A helper method to view transation id """
        return str(self.id)

    @property
    def get_cart_tot(self):
        orderitems = self.ordereditems_set.all()
        total = sum([item.get_total_price for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.ordereditems_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderedItems(models.Model):
    """ A model of ordered items """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)
    added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        """ A method to get the total price """
        total = self.product.price * self.quantity
        return total


class ShippingDetails(models.Model):
    """ A model for shipping details """
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    street_address1 = models.CharField(max_length=150, null=True)
    street_address2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    state_or_country = models.CharField(max_length=150, null=True)
    zip_or_eircode = models.CharField(max_length=150, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ A helper method to see the address """
        return self.street_address1






