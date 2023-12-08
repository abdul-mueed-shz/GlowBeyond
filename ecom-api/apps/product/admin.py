from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        "category",
        "name",
        "slug",
        "description",
        "price",
        "image",
        "thumbnail",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "slug",
    ]
