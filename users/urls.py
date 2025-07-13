from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('', views.home, name="home"),
    path('logout/', views.logout_view, name="logout_view")]