from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, Topping
from bag.contexts import bag_contents
from decimal import Decimal

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_list in bag.items():
                product = Product.objects.get(id=item_id)
                for item in item_list:
                    try:
                        selected_toppings = None
                        if len(item['additional_toppings']) > 0:
                            if len(item['additional_toppings']) > 1:
                                selected_toppings = Topping.objects.filter(id__in=item['additional_toppings'])
                            else:
                                selected_toppings = Topping.objects.filter(id=item['additional_toppings'][0])

                        toppings_price = 0
                        if selected_toppings is not None:
                            toppings_price = sum(int(topping.price) for topping in selected_toppings.all()) * item['quantity']

                        if item['size'] == '30':
                            lineitem_total = product.price * item['quantity'] + toppings_price
                        elif item['size'] == '35':
                            toppings_price = toppings_price * Decimal(1.1)
                            lineitem_total = (product.price * Decimal(1.1)) * item['quantity'] + toppings_price
                        elif item['size'] == '40':
                            toppings_price = toppings_price * Decimal(1.3)
                            lineitem_total = (product.price * Decimal(1.3)) * item['quantity'] + toppings_price

                        try:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                product_size=item['size'],
                                quantity=item['quantity'],
                                lineitem_total=round(lineitem_total, 2),
                            )

                            order_line_item.save()
                            
                            if selected_toppings is not None:
                                order_line_item.toppings.set(selected_toppings)
                                order_line_item.save()
                        except Exception as e:
                            messages.error(request, f'An error occurred while saving your order. \
                                Please try again later. {e}')
                            order.delete()
                            return redirect(reverse('view_bag'))

                    except Product.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your bag wasn't found in our database. "
                            "Please call us for assistance!")
                        )
                        order.delete()
                        return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('pizza_list'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)