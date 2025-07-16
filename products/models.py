from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

