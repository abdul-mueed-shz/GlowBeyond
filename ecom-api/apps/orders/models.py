from django.db import models
from django.contrib.auth.models import User
from apps.commons.models import BaseModel
from apps.payment.models import PaymentMethod
from apps.product.models import Product

DELIVERY_STATUS = [
    ("PENDING", "Pending"),
    ("PROCESSING", "Processing"),
    ("SHIPPED", "Shipped"),
    ("OUT_FOR_DELIVERY", "Out for Delivery"),
    ("DELIVERED", "Delivered"),
    ("CANCELLED", "Cancelled"),
    ("RETURNED", "Returned"),
]


class DeliveryStatus(models.Model):
    name = models.CharField(max_length=255, choices=DELIVERY_STATUS, unique=True)

    class Meta:
        db_table = "delivery-status"
        verbose_name = "Delivery Status"
        verbose_name_plural = "Delivery Statuses"

    def __str__(self):
        return self.name


class Customer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
    )
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    delivery_status = models.ForeignKey(
        DeliveryStatus, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "order"
        ordering = ("-created_on",)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "order-items"
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
