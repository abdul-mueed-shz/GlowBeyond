from django.db import models
from django.contrib.auth.models import User
from apps.commons.models import BaseModel
from apps.product.models import Product


class Orders(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        # unique=True,
    )
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.PositiveIntegerField()
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # stripe_token = models.CharField(max_length=250)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.first_name


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
