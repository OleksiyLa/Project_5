from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product, Topping
from decimal import Decimal

import json
import time
import stripe

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_list in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    for item in item_list:
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
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)