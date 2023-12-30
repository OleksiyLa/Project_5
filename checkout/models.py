import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product, Topping
from decimal import Decimal


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False, default="Ireland")
    county = models.CharField(max_length=80, null=False, blank=False, default="County Kerry")
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default="Tralee")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < 50:
            self.delivery_cost = 12
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=True, blank=False, on_delete=models.SET_NULL)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    toppings = models.ManyToManyField(Topping)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        toppings_price = sum(int(topping.price) for topping in self.toppings.all())
        if self.product_size == '30':
            self.lineitem_total = self.product.price * self.quantity + toppings_price
        if self.product_size == '35':
            toppings_price = toppings_price * Decimal(1.1)
            self.lineitem_total = self.product.price * Decimal(1.1) * self.quantity + toppings_price
        if self.product_size == '40':
            toppings_price = toppings_price * Decimal(1.3)
            self.lineitem_total = self.product.price * Decimal(1.3) * self.quantity + toppings_price
        super().save(*args, **kwargs)
