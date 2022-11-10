from rest_framework import serializers
from ..models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'slug',
            'description',
            'price',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        )
