from apps.info.api.serializers import (
    AppSerializer,
    ContactInformationSerializer,
    MailingInformationSerializer,
    SocialSerializer,
)
from apps.info.models import App, ContactInformation, MailingInformation, Social
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


class MailingInfoViewSet(ReadOnlyModelViewSet):
    serializer_class = MailingInformationSerializer

    def get_queryset(self):
        return MailingInformation.objects.all()


class ContactInfoViewSet(ReadOnlyModelViewSet):
    serializer_class = ContactInformationSerializer

    def get_queryset(self):
        return ContactInformation.objects.all()
