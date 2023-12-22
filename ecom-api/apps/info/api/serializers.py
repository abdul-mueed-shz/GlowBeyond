from rest_framework import serializers
from apps.info.models import App, Social


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
