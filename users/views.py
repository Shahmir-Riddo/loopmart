from django.contrib.auth import authenticate, login as login_auth
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as login_auth, logout
# from .utils import generate_otp, verify_otp
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from .models import Profile
import random
from cart.models import Cart, CartItems
from django.contrib.auth.models import User
from .decorators import user_is_owner
from django.db.models import Sum


@login_required
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()
            if user is not None:
                login_auth(request, user)
                return redirect("/")
            else:
                return HttpResponse("Wrong Credentials")


    else:
        form = LoginForm()

    
    context = {'form': form}
    return render(request, 'login.html', context)



def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("✅ User created:", user)
            return redirect('/auth/login')
        else:
            print(":{ User not created:")
    else:

        form = SignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('auth/')


def otp_verify(request):
    pass

@login_required
@user_is_owner
def profile(request, username):

    user = get_object_or_404(User, username=username)
    profile_obj = Profile.objects.get(user=user)
    cart = Cart.objects.get(user=user)
    cart_items = cart.items.all()
    carts = Cart.objects.filter(user=user).annotate(total_price=Sum('items__cart_items__price'))
    context =  {
        'profile': profile_obj,
        'cart': cart,
        'cart_items': cart_items,
        'carts': carts
    }

    return render(request, 'profile.html', context)
