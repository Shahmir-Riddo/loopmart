from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('update_cart', views.update_cart, name='update_cart',),
    path('delete_cart_item', views.delete_cart_item, name='delete_cart_item')
        
]