from django.contrib import admin

from apps.mailing.models import EmailStatus, Mailing

# Register your models here.
admin.site.register(EmailStatus)
admin.site.register(Mailing)
