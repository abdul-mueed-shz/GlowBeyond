import stripe
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.commons.utils.auth import JwtAuthentication
from apps.orders.models import Orders, OrderItems
from apps.product.api.serializers import ProductSerializer
from apps.product.models import Product

from apps.orders.api.serializers import OrderSerializer, OrderItemSerializer
from apps.user.api.serializers import UserSerializer
from django.conf import settings


class CheckoutView(APIView):
    authentication_classes = (JwtAuthentication,)

    def post(self, request):
        request_data = request.data
        try:
            products = request_data.pop('products')
            order_details = request_data
        except NotFound:
            raise NotFound("Product key not found")

        order_serializer = OrderSerializer(data=order_details)
        order_serializer.is_valid(raise_exception=True)
        order_object = order_serializer.save()

        for product in products:
            data = {
                'order': order_object.id,
                'product': product['id'],
                'quantity': product['quantity'],
            }
            order_item_serializer = OrderItemSerializer(data=data)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save()

        # stripe.api_key = settings.STRIPE_SECRET_KEY
        return Response(order_serializer.data)


class ConsumedProducts(APIView):
    authentication_classes = (JwtAuthentication,)

    def get(self, request):
        user_id = request.query_params.get("id")
        if not user_id:
            raise ValidationError("User id is mandatory")
        user_orders = Orders.objects.filter(user=user_id)
        response = Response()
        if len(user_orders) <= 0:
            response.data({
                "message": "No products bought!"
            })
            return response
        orders = {}
        for order in user_orders:
            order_items = OrderItems.objects.filter(order=order.id)
            products = []
            for item in order_items:
                product_data = ProductSerializer(item.product).data
                product_data["quantity"] = item.quantity
                products.append(product_data)
            orders[order.id] = {
                "products": products,
                "payed_amount": order.paid_amount
            }

        return Response(orders)
