from rest_framework import serializers
from apps.info.models import (
    App,
    BannerItem,
    ContactInformation,
    MailingInformation,
    Social,
)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"


class MailingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingInformation
        fields = "__all__"


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = "__all__"


class BannerItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = BannerItem
        fields = "__all__"
