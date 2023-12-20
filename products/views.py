from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProduct

# Create your views here.


def pizza_list(request):
    products = Product.objects.all()
    return render(request, 'products/pizza_list.html', {'products': products})

def add_pizza(request):
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    return render(request, 'products/pizza_add.html', {'form': form})
