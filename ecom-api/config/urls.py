from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_prefix = 'api/v1/'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(api_prefix, include('apps.orders.api.urls')),
                  path(api_prefix, include('djoser.urls')),
                  path(api_prefix, include('djoser.urls.authtoken')),
                  path(api_prefix, include('apps.commons.api.urls')),
                  path(api_prefix, include('apps.product.api.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
