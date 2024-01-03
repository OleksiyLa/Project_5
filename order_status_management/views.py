from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product, Topping
from products.forms import AddProduct, PizzaFilterForm, AddTopping
from checkout.models import Order


def orders(request):
    orders = Order.objects.all().order_by('-created_at')


    return render(request, 'order_status_management/orders.html', {'orders': orders, 'active_link': 'orders'})