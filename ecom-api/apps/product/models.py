from django.db import models

from config.settings.base import APP_URL
from ..commons.models import BaseModel
from apps.commons.utils.functions import make_thumbnail


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField()

    class Meta:
        db_table = "category"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(BaseModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=225)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)

    class Meta:
        db_table = "product"
        ordering = ("-created_on",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_images(self):
        attachments = self.attachment_set.all()
        file_urls = []
        if len(attachments):
            for attachment in attachments:
                file_urls.append(APP_URL + attachment.file.url)
            return file_urls
        return file_urls

    def get_thumbnail(self):
        if self.thumbnail:
            return APP_URL + self.thumbnail.url
        else:
            attachments = self.attachment_set.all()
            if len(attachments):
                image = attachments[0]
                self.thumbnail = make_thumbnail(image)
                self.save()
                return APP_URL + self.thumbnail.url
            else:
                return ""


ATTACHMENT_CHOICES = (
    ("IMAGE", "IMAGE"),
    ("VIDEO", "VIDEO"),
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return "product_attachment/{0}/{1}".format(instance.product.id, filename)


class Attachment(BaseModel):
    file = models.FileField("Attachment", upload_to=user_directory_path)
    file_type = models.CharField("File type", choices=ATTACHMENT_CHOICES, max_length=10)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )

    class Meta:
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"

    def __str__(self) -> str:
        return f"{self.product.name}_{self.file_type.lower()}"
