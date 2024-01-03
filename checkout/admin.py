from django.contrib import admin
from .models import Order, OrderLineItem
from order_status_management.models import OrderProgress


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created_at',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'created_at', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid', 'progress')

    list_display = ('order_number', 'created_at', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'progress')

    ordering = ('-created_at',)

admin.site.register(Order, OrderAdmin)
