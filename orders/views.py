from django.shortcuts import redirect, get_object_or_404, render

from cart.models import Cart, CartItems
from .models import Order, OrderItem
from .forms import CheckoutForm
# Create your views here.
def checkout(request):
    if request.method == "POST":
        form = CheckoutForm()

    user = request.user
    cart = Cart.objects.get(user=user)  
    items = cart.items.all()
    

    if not items.exist():
        return redirect('cart')
    
    order = Order.objects.create(user=user)

    for item in items:
        OrderItem.objects.create(
            product = item.product,
            order = order,
            price = item.product.price,
            quantity = item.product.quantity,
        )
    items.delete()

    return redirect('order_details', order_id=order.id)


def order_detail(requests, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render('order_detail.html')

