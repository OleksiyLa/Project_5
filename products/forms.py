from django import forms
from .models import Product


class AddProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'rating', 'image', 'is_spicy', 'is_vegetarian', 'is_premium', 'is_seafood', 'is_new']
