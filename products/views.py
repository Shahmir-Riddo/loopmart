from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Avg, Max, Count
from cart.models import Cart, CartItems
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):

    


    categories = Category.objects.all().annotate(product_count=Count("product")).prefetch_related("product_set")

    products = Product.objects.all().order_by("price").select_related("category")
    avg_price = products.aggregate(Avg("price", default=0))['price__avg']
    max_price = products.aggregate(Max("price"))['price__max']

    context = {
                'products': products,
                'categories': categories,
                'avg_price': avg_price,
                'max_price': max_price
               }
    
    return render(request, 'index.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


def category_view(request, category_name):
    category = Category.objects.get(title=category_name)
    print(category.is_active)
    category_products = Product.objects.filter(category=category)
    print(category_products)
    

    context = {
        'category': category,
        'products': category_products
    }

    return render(request, 'category_products.html', context)

@require_POST
@login_required
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    items, created = CartItems.objects.get_or_create(cart=cart, cart_items=product)

    return redirect(f'/accounts/profile/{request.user.username}')