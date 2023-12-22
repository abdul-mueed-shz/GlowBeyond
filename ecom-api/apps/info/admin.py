from django.contrib import admin

from apps.info.models import App, Social

# Register your models here.
admin.site.register(Social)
admin.site.register(App)
