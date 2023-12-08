from django.contrib import admin

from apps.orders.models import Customer, Order, OrderItems

# Register your models here.
admin.site.register(Customer)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1  # Number of empty forms to display for adding new OrderItems


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    list_display = ("customer", "paid_amount", "display_order_items")

    def display_order_items(self, obj):
        # Retrieve related OrderItems and format them as a string
        order_items = OrderItems.objects.filter(order=obj)
        return ", ".join([f"{item.quantity} x {item.product}" for item in order_items])

    display_order_items.short_description = "Order Items"


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)
