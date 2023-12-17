from apps.info.api.serializers import AppSerializer, SocialSerializer
from apps.info.models import App, Social
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.
class SocialsView(ReadOnlyModelViewSet):
    serializer_class = SocialSerializer

    def get_queryset(self):
        return Social.objects.all()


class AppInfoView(ReadOnlyModelViewSet):
    serializer_class = AppSerializer

    def get_queryset(self):
        return App.objects.all()
