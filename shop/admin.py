from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'customer_name',
        'address',
        'total_cost',
        'payment_method',
        'is_paid',
        'created_at'
    ]
    list_filter=['is_paid','payment_method']
    search_fields=('customer_name','address')
    ordering=['-created_at']

admin.site.register(Order, OrderAdmin)