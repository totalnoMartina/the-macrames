from django.contrib import admin
from .models import Customer, Product, Ordering, Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Ordering)
admin.site.register(Tag)