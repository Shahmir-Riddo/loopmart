from django import forms
from .models import Order, OrderItem

class CheckoutForm(forms.Form):
    class Meta:
        model = Order
        fields = []