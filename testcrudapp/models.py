from django.db import models

class Customer(models.Model):
    """ A class to hold info on Customers """

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """ A helper method to see the name """
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ A class to hold info on the Product """
    CATEGORY = (
        ('Outdoor:', 'Outdoor'),
        ('Indoor', 'Indoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name





class Ordering(models.Model):
    """ The class to hold the info on the order """
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(null=True, choices=STATUS, max_length=200)    


    def __str__(self):
        return self.product

