from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProduct, PizzaFilterForm

# Create your views here.


def pizza_list(request):
    form = PizzaFilterForm(request.GET)
    if form.is_valid():
        is_spicy = form.cleaned_data.get('is_spicy')
        is_vegetarian = form.cleaned_data.get('is_vegetarian')
        is_premium = form.cleaned_data.get('is_premium')
        is_seafood = form.cleaned_data.get('is_seafood')
        is_new = form.cleaned_data.get('is_new')

        filters = {}
        if is_spicy:
            filters['is_spicy'] = is_spicy
        if is_vegetarian:
            filters['is_vegetarian'] = is_vegetarian
        if is_premium:
            filters['is_premium'] = is_premium
        if is_seafood:
            filters['is_seafood'] = is_seafood
        if is_new:
            filters['is_new'] = is_new

        if any(filters.values()):
            products = Product.objects.filter(**filters)
        else:
            products = Product.objects.all()

    return render(request, 'products/pizza_list.html', {'products': products, 'form': form})


def add_pizza(request):
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    return render(request, 'products/pizza_add.html', {'form': form})
