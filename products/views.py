from django.shortcuts import render
from .models import Product, Category
from django.db.models import Avg, Max, Count
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