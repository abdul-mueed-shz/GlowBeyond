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
