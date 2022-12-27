from rest_framework import serializers
from ..models import Orders, OrderItems
from ...product.api.serializers import ProductSerializer
from django.contrib.auth.models import User

from ...product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(read_only=False, many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Orders
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'city',
            'zip_code',
            'user',
            # 'stripe_token',
            'paid_amount',
            # 'products',
        )


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Orders.objects.all(), many=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False)

    class Meta:
        model = OrderItems
        fields = (
            'order',
            'product',
            'quantity'
        )
