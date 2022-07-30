from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shopping_cart/', views.shopping_cart, name='shopping-cart'),
    path('checkout/', views.checkout, name='checkout'),

]
