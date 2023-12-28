from django.shortcuts import render, redirect, reverse, HttpResponse
import uuid


def view_bag(request):
    """ A view that renders the cart page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    if request.method == 'POST':
        size = request.POST.get('selected_size')
        additional_toppings = request.POST.get('additional_toppings')
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})
        sorted_toppings_list = []
        if additional_toppings:
            sorted_toppings_list = sorted(additional_toppings.split(','))

        if item_id in bag:
            pizzas_by_size = [pizza for pizza in bag[item_id] if pizza['size'] == size]
            if len(pizzas_by_size) > 0:
                flag = True
                for pizza in pizzas_by_size:
                    sorted_toppings = sorted(pizza['additional_toppings'])
                    if sorted_toppings == sorted_toppings_list:
                        pizza['quantity'] += 1
                        flag = False
                        break
                if flag:
                    bag[item_id].append({
                        'id': str(uuid.uuid4()),
                        'size': size,
                        'additional_toppings': sorted_toppings_list,
                        'quantity': 1
                    })       
            else:
                bag[item_id].append({
                    'id': str(uuid.uuid4()),
                    'size': size,
                    'additional_toppings': sorted_toppings_list,
                    'quantity': 1
                })
        else:
            bag[item_id] = [{
                'id': str(uuid.uuid4()),
                'size': size,
                'additional_toppings': sorted_toppings_list,
                'quantity': 1
            }]

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    id = request.POST.get('id')
    bag = request.session.get('bag', {})
    for pizza in bag[item_id]:
        if pizza['id'] == id:
            pizza['quantity'] = quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id, id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag[item_id] = [pizza for pizza in bag[item_id] if pizza['id'] != id]

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        return HttpResponse(status=500)
