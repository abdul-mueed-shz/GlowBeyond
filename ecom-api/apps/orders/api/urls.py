from .views import CheckoutView, ConsumedProducts
from django.urls import path

urlpatterns = [
    path('checkout', CheckoutView.as_view()),
    path('consumed-products', ConsumedProducts.as_view()),
]
