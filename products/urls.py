from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('products/', views.index, name='index'),
    path('product/<slug:product_slug>', views.product_detail, name='product_detail'),
    path('category/<slug:category_name>', views.category_view, name='category_view'),
    path('cart/add', views.add_to_cart, name='add_to_cart')
]