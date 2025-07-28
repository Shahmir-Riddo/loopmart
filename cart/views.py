from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import Cart, CartItems
from users.decorators import user_is_owner
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views
@login_required(login_url='/accounts/login/')
def cart(request):
    username= request.user.username
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

    return render(request, 'cart.html', context)


def update_cart(request):
    quantity = request.POST.get('quantity')
    cart_item_id = request.POST.get('cart_item_id')
    cart_item_obj = CartItems.objects.get(id=cart_item_id)
    cart_item_obj.quantity = quantity
    cart_item_obj.save()

    return redirect('/cart')


def delete_cart_item(request):
    user = User.objects.get(username=request.user.username)
    cart = Cart.objects.get(user=user)
    

    cart_item_id = request.POST.get('cart_item_id')
    print(cart_item_id)
    cart_item_obj = cart.items.get(id=cart_item_id)
    cart_item_obj.delete()


    
    
    return redirect('/cart')