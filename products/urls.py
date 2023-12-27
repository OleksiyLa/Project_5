from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('add_pizza', views.add_pizza, name='add_pizza'),
    path('add_topping', views.add_topping, name='add_topping'),
    path('pizza_detail/<slug:slug>', views.pizza_detail, name='pizza_detail'),
    ]
