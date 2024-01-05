from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from checkout.models import Order


def order_tracker(request):
    if request.POST:
        order_number = request.POST['order_number']
        order = Order.objects.filter(order_number=order_number).exists()

        if order:
            order = Order.objects.get(order_number=order_number)
            if order.progress.is_active:
                timestamp = int(order.progress.new_at.timestamp())
                return redirect('order_tracker_bar', order_number=order.order_number, timestamp=timestamp)
            else:
                messages.error(request, 'Order not found')
                return redirect('order_tracker')
        else:
            messages.error(request, 'Order not found')
            return redirect('order_tracker')

    return render(request, 'order_tracker/order_tracker.html', {'active_link': 'tracker'})


def order_tracker_bar(request, order_number, timestamp):    
    order = get_object_or_404(Order, order_number=order_number, progress__is_active=True)

    if int(order.progress.new_at.timestamp()) != int(timestamp):
        raise Http404('Order not found')

    status = order.progress.status

    time_taken = None
    status_name = 'Pending'

    if status == 'accepted':
        status_name = 'Accepted'
    elif status == 'being_cooked':
        status_name = 'Cooking'
    elif status == 'being_prepared':
        status_name = 'Preparing'
    elif status == 'being_delivered':
        status_name = 'Delivering'
    elif status == 'completed':
        status_name = 'Delivered'
        time_taken = order.progress.completed_at - order.progress.new_at
        time_taken = time_taken.total_seconds() // 60
        time_taken = str(time_taken).split('.')[0]

    return render(request, 'order_tracker/order_tracker_bar.html', {'status': status, 'status_name': status_name, 'order': order, 'active_link': 'tracker', 'time_taken': time_taken})