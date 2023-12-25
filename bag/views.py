from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the cart page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product_id = request.POST.get('product_id')
    size = request.POST.get('selected_size')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += 1
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
