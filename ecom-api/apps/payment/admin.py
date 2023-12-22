from django.contrib import admin

from apps.payment.models import PaymentMethod

# Register your models here.
admin.site.register(PaymentMethod)
