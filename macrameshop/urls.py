from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.AddToCart.as_view(), name ='add'),
    path('shopping_cart/', views.shopping_cart, name='shopping-cart'),
    path('checkout/', views.checkout, name='checkout'),

]
