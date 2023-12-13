from rest_framework import serializers

from apps.payment.models import PaymentMethod
from ..models import Customer, DeliveryStatus, Order, OrderItems
from ...product.models import Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), many=False
    )
    payment_method = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=PaymentMethod.objects.all(),
        many=False,
        default=PaymentMethod.objects.get(name="COD"),
    )
    delivery_status = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=DeliveryStatus.objects.all(),
        many=False,
        default=DeliveryStatus.objects.get(name="PENDING"),
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=False)
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=False
    )

    class Meta:
        model = OrderItems
        fields = ("order", "product", "quantity")
