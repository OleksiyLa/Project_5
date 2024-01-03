from django.shortcuts import render, redirect
from checkout.models import Order

def order_tracker(request):
    if request.POST:
        order_number = request.POST['order_number']
        return redirect('order_tracker_bar', order_number) 

    return render(request, 'order_tracker/order_tracker.html', {'active_link': 'tracker'})


def order_tracker_bar(request, order_number):    
    order = Order.objects.get(order_number=order_number)
    status = order.progress.status
    

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

    return render(request, 'order_tracker/order_tracker_bar.html', {'status': status, 'status_name': status_name, 'order': order, 'active_link': 'tracker'})