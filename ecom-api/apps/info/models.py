from django.db import models

from apps.commons.models import BaseModel
from config.settings.base import APP_URL


# Create your models here.
class Social(BaseModel):
    mdi_icon = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=500)

    class Meta:
        db_table = "social"
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self) -> str:
        return self.name


def app_directory_path(_, filename):
    return "app/{0}".format(filename)


class App(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=app_directory_path, blank=True, null=True)

    class Meta:
        db_table = "app_info"
        verbose_name = "App"
        verbose_name_plural = "App"

    def get_logo(self):
        if self.thumbnail:
            return APP_URL + self.logo.url
        return ""

    def __str__(self) -> str:
        return self.name


class MailingInformation(BaseModel):
    info = models.CharField(max_length=1000)

    class Meta:
        db_table = "mailing_information"
        verbose_name = "Mailing Information"
        verbose_name_plural = "Mailing Informations"

    def __str__(self) -> str:
        return self.info


class ContactInformation(BaseModel):
    info = models.CharField(max_length=1000)

    class Meta:
        db_table = "contact_information"
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"

    def __str__(self) -> str:
        return self.info


def banner_directory_path(instance, filename):
    return "banner_image/{0}".format(filename)


class BannerItem(BaseModel):
    heading = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to=banner_directory_path)

    class Meta:
        db_table = "banner_item"
        verbose_name = "Banner Item"
        verbose_name_plural = "Banner Items"

    def __str__(self) -> str:
        return self.heading

    def get_image(self):
        if self.image:
            return APP_URL + self.image.url


class BannerNotification(BaseModel):
    statement = models.CharField(max_length=1000)

    class Meta:
        db_table = "banner-notification"
        verbose_name = "Banner Notification"
        verbose_name_plural = "Banner Notifications"

    def __str__(self) -> str:
        return self.statement

    def save(self, *args, **kwargs):
        if BannerNotification.objects.filter().exists():
            return
        super(BannerNotification, self).save(*args, **kwargs)
