from django.contrib import admin

from apps.info.models import (
    App,
    BannerItem,
    BannerNotification,
    ContactInformation,
    MailingInformation,
    Social,
)

# Register your models here.
admin.site.register(Social)
admin.site.register(App)
admin.site.register(MailingInformation)
admin.site.register(ContactInformation)
admin.site.register(BannerItem)
admin.site.register(BannerNotification)
