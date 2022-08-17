from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    # path('add/', views.AddToCart.as_view(), name ='add'),
    # path('shopping_cart/', views.shopping_cart, name='shopping-cart'),
    # path('checkout/', views.checkout, name='checkout'),

]