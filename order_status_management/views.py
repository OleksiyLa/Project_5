from django.shortcuts import render, redirect
from django.db.models import Q
from checkout.models import Order


def orders(request, status):    
    orders = Order.objects.filter(progress__status=status, progress__is_active=True).order_by('-created_at')

    return render(request, 'order_status_management/orders.html', {'orders': orders, 'status': status})


def proceed(request, order_number):
    order = Order.objects.get(order_number=order_number)
    prev_status = order.progress.status
    print(prev_status)
    if prev_status == 'new':
        order.progress.status = 'accepted'
    if prev_status == 'accepted':
        order.progress.status = 'being_cooked'
    if prev_status == 'being_cooked':
        order.progress.status = 'being_prepared'
    if prev_status == 'being_prepared':
        order.progress.status = 'being_delivered'
    if prev_status == 'being_delivered':
        order.progress.status = 'completed'
    if prev_status == 'completed':
        order.progress.is_active = False
    order.progress.save()
    return redirect('orders', prev_status)