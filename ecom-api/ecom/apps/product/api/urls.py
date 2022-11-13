from .views import FetchLatestProducts, FetchCategories, Search

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', FetchLatestProducts, basename='product')
router.register(r'categories', FetchCategories, basename='categories')
router.register(r'', Search, basename='search')

urlpatterns = [
    # path('latest-products/', LatestProductList.as_view()),
    path('', include(router.urls), ),
]
