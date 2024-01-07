from django import forms
from .widgets import CustomCloudinaryField
from .models import Product, Topping


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'price',
                  'image',
                  'is_spicy',
                  'is_vegetarian',
                  'is_premium',
                  'is_seafood',
                  'is_new']

    image = CustomCloudinaryField(label='Image',
                                  required=False)


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name', 'price', 'image']

    image = CustomCloudinaryField(label='Image',
                                  required=False)


class PizzaFilterForm(forms.Form):
    is_spicy = forms.BooleanField(label='Spicy',
                                  required=False)
    is_vegetarian = forms.BooleanField(label='Vegetarian',
                                       required=False)
    is_premium = forms.BooleanField(label='Premium',
                                    required=False)
    is_seafood = forms.BooleanField(label='Seafood',
                                    required=False)
    is_new = forms.BooleanField(label='New',
                                required=False)
