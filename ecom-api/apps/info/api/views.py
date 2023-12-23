from apps.info.api.serializers import (
    AppSerializer,
    BannerItemSerialzer,
    BannerNotificationSerializer,
    ContactInformationSerializer,
    MailingInformationSerializer,
    SocialSerializer,
)
from apps.info.models import (
    App,
    BannerItem,
    BannerNotification,
    ContactInformation,
    MailingInformation,
    Social,
)
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.
class SocialsView(ReadOnlyModelViewSet):
    serializer_class = SocialSerializer

    def get_queryset(self):
        return Social.objects.filter(isActive=True, isDeleted=False)


class AppInfoView(ReadOnlyModelViewSet):
    serializer_class = AppSerializer

    def get_queryset(self):
        return App.objects.filter(isActive=True, isDeleted=False)


class MailingInfoViewSet(ReadOnlyModelViewSet):
    serializer_class = MailingInformationSerializer

    def get_queryset(self):
        return MailingInformation.objects.filter(isActive=True, isDeleted=False)


class ContactInfoViewSet(ReadOnlyModelViewSet):
    serializer_class = ContactInformationSerializer

    def get_queryset(self):
        return ContactInformation.objects.filter(isActive=True, isDeleted=False)


class BannerItemViewset(ReadOnlyModelViewSet):
    serializer_class = BannerItemSerialzer

    def get_queryset(self):
        return BannerItem.objects.filter(isActive=True, isDeleted=False)


class BannerNotificationViewset(ReadOnlyModelViewSet):
    serializer_class = BannerNotificationSerializer

    def get_queryset(self):
        return BannerNotification.objects.filter(isActive=True, isDeleted=False)
