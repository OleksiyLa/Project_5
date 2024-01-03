from django.shortcuts import render, redirect
from django.db.models import Q
from checkout.models import Order


def orders(request, status):    
    orders = Order.objects.filter(progress__status=status).order_by('-created_at')

    return render(request, 'order_status_management/orders.html', {'orders': orders, 'status': status})