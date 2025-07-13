from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('products/', views.index, name='index'),
]