from django.shortcuts import render

# Create your views here.


def pizza_list(request):
    return render(request, 'products/pizza_list.html')