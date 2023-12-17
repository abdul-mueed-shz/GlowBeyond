import stripe
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from apps.commons.utils.auth import JwtAuthentication
from apps.orders.models import DeliveryStatus, Order, OrderItems
from apps.payment.models import PaymentMethod
from apps.product.api.serializers import ProductSerializer
from apps.product.models import Product

from apps.orders.api.serializers import (
    CustomerSerializer,
    OrderSerializer,
    OrderItemSerializer,
)
from django.db import transaction


class CheckoutView(GenericAPIView):
    DEFAULT_DELIVERY_STATUS = DeliveryStatus.objects.filter(name="PENDING")
    DEFAULT_PAYMENT_METHOD = PaymentMethod.objects.filter(name="COD")

    def check_order_and_add_defaults(self, order_data):
        if (
            not order_data.get("payment_method")
            and self.DEFAULT_PAYMENT_METHOD.exists()
        ):
            order_data.update(
                {"payment_method": self.DEFAULT_PAYMENT_METHOD.first().id}
            )

        if (
            not order_data.get("delivery_status")
            and self.DEFAULT_DELIVERY_STATUS.exists()
        ):
            order_data.update(
                {"delivery_status": self.DEFAULT_DELIVERY_STATUS.first().id}
            )

        return order_data

    @transaction.atomic
    def post(self, request):
        request_data = request.data.copy()
        customer_data = request_data.get("customer")
        products = request_data.get("products")
        order_data = request_data.get("order")

        if not customer_data or not len(products) or not order_data:
            raise ValidationError("Invalid order details")

        customer_serializer = CustomerSerializer(data=customer_data)
        customer_serializer.is_valid(raise_exception=True)
        customer_instance = customer_serializer.save()

        self.check_order_and_add_defaults(order_data=order_data)

        order_data = {"customer": customer_instance.id, **order_data}
        order_serializer = OrderSerializer(data=order_data)
        order_serializer.is_valid(raise_exception=True)
        order_instance = order_serializer.save()

        order_items = []
        for product in products:
            order_item_data = {
                "order": order_instance.id,
                "product": product.get("id"),
                "quantity": product.get("quantity"),
            }
            order_items.append(order_item_data)

        order_item_serializer = OrderItemSerializer(data=order_items, many=True)
        order_item_serializer.is_valid(raise_exception=True)
        order_item_serializer.save()
        return Response(order_serializer.data)


class ConsumedProducts(GenericAPIView):
    authentication_classes = (JwtAuthentication,)

    def get(self, request):
        user_id = request.query_params.get("id")
        if not user_id:
            raise ValidationError("User id is mandatory")
        user_orders = Order.objects.filter(user=user_id)
        response = Response()
        if len(user_orders) <= 0:
            response.data({"message": "No products bought!"})
            return response
        orders = {}
        for order in user_orders:
            order_items = OrderItems.objects.filter(order=order.id)
            products = []
            for item in order_items:
                product_data = ProductSerializer(item.product).data
                product_data["quantity"] = item.quantity
                products.append(product_data)
            orders[order.id] = {"products": products, "payed_amount": order.paid_amount}

        return Response(orders)
