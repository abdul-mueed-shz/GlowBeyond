from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category


# Create your views here.
# class LatestProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()[:4]
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

class FetchCategories(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class FetchLatestProducts(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()[:4]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def product_details(self, request):
        query_params = request.query_params
        try:
            category_slug = query_params['category_slug']
            product_slug = query_params['product_slug']
            queryset = Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
            serializer = ProductSerializer(queryset)
            print(serializer)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'Error': 'Http404'})

    #
    # def retrieve(self, request, pk=None):
    #     querydict = request.query_params
    #     # cat = querydict['category_slug']
    #     # bat = querydict['product_slug']
    #     # products.objects.filter(category__slug=querydict['category_slug']).get()
    #     queryset = Product.objects.all()
    #     product = get_object_or_404(queryset, pk=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
