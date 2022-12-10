from rest_framework import serializers
from ..models import Orders
from ...product.api.serializers import ProductSerializer
from ...user.api.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=False, many=True)
    user = UserSerializer(read_only=False)

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
            'stripe_token',
            'paid_amount',
            'products',
        )
