from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from apps.info.api.views import AppInfoView, SocialsView

api_prefix = "api/v1/"

router = DefaultRouter()
router.register(api_prefix + "socials", SocialsView, basename="socials")
router.register(api_prefix + "app-info", AppInfoView, basename="app_info")

urlpatterns = [
    path("admin/", admin.site.urls),
    path(api_prefix, include("apps.orders.api.urls")),
    path(api_prefix, include("djoser.urls")),
    path(api_prefix, include("djoser.urls.authtoken")),
    path(api_prefix, include("apps.commons.api.urls")),
    path(api_prefix, include("apps.product.api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
