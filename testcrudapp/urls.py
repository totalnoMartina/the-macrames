from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    # path('add/', views.AddToCart.as_view(), name ='add'),
    # path('shopping_cart/', views.shopping_cart, name='shopping-cart'),
    # path('checkout/', views.checkout, name='checkout'),

]