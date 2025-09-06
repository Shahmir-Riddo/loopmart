from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "orders"

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order_detail/<order_id>', views.order_detail, name='order_detail',),
        
]