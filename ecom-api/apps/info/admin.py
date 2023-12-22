from django.contrib import admin

from apps.info.models import App, ContactInformation, MailingInformation, Social

# Register your models here.
admin.site.register(Social)
admin.site.register(App)
admin.site.register(MailingInformation)
admin.site.register(ContactInformation)
