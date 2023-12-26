from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    price = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, sizes in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        print(f"Item ID: {item_id}, Sizes: {sizes}")
        for size, quantity in sizes.items():
            print(f"Size: {size}, Quantity: {quantity}, product.price: {product.price}")
            if size == '30':
                price = quantity * product.price
                total += quantity * product.price
            if size == '35':
                price = quantity * product.price * Decimal(1.1)
                total += quantity * product.price * Decimal(1.1)
            if size == '40':
                price = quantity * product.price * Decimal(1.3)
                total += quantity * product.price * Decimal(1.3)
            
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'size': size,
                'quantity': quantity,
                'product': product,
                'price': round(price, 2),
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': round(total, 2),
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': round(grand_total, 2),
    }

    return context