from django.db import models


# Create your models here.
class PaymentMethod(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("CREDIT_CARD", "Credit Card"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("COD", "Cash on delivery"),
    ]
    name = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES, unique=True)

    class Meta:
        db_table = "payment-method"
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"

    def __str__(self):
        return self.name
