from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view that renders the cart page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    if request.method == 'POST':
        size = request.POST.get('selected_size')
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})
        print(size)
        if item_id in bag:
            if size in bag[item_id]:
                bag[item_id][size] += 1
            else:
                bag[item_id][size] = 1
        else:
            bag[item_id] = {size: 1}

    request.session['bag'] = bag
    print('get', request.GET)
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')

    bag = request.session.get('bag', {})
    bag[item_id][size] = quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id, item_size):
    """Remove the item from the shopping bag"""

    try:
        # size = request.POST['product_size']
        print(item_size)
        bag = request.session.get('bag', {})
        del bag[item_id][item_size]

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        return HttpResponse(status=500)
