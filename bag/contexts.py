from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product, Topping


def bag_contents(request):

    deliver_cost = Decimal('12.00')
    free_delivery_threshold = Decimal('50.00')
    bag_items = []
    total = 0
    price = 0
    product_count = 0
    
    bag = request.session.get('bag', {})

    for item_id, item_list in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        for item in item_list:
            if len(item['additional_toppings']) == 0:
                toppings = []
                toppings_price = 0
            elif len(item['additional_toppings']) == 1:
                toppings = [get_object_or_404(Topping, pk=item['additional_toppings'][0])]
                toppings_price = int(toppings[0].price)
            else:
                toppings = Topping.objects.filter(id__in=item['additional_toppings'])
                toppings_price = sum(int(item.price) for item in toppings)
            if item['size'] == '30':
                price = item['quantity'] * (product.price + toppings_price)
                total += price
            if item['size'] == '35':
                price = item['quantity'] * (product.price + toppings_price) * Decimal(1.1)
                total += price
            if item['size'] == '40':
                price = item['quantity'] * (product.price + toppings_price) * Decimal(1.3)
                total += price
            topping_names = [topping.name for topping in toppings]
            product_count += item['quantity']
            bag_items.append({
                'item_id': item_id,
                'id': item['id'],
                'size': item['size'],
                'quantity': item['quantity'],
                'product': product,
                'toppings': ', '.join(topping_names),
                'price': round(price, 2),
            })

    if total >= free_delivery_threshold:
        deliver_cost = Decimal('0.00')  

    grand_total = deliver_cost + Decimal(total)

    context = {
        'bag_items': bag_items,
        'total': round(total, 2),
        'product_count': product_count,
        'deliver_cost': deliver_cost,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': round(grand_total, 2),
    }

    return context
