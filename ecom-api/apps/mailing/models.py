from django.db import models

from apps.commons.models import BaseModel


EMAIL_STATUS_CHOICES = [
    ("PENDING", "pending"),
    ("SENT", "sent"),
    ("FAILED", "failed"),
    ("RETRY", "retry"),
]


# Create your models here.
class EmailStatus(models.Model):
    name = models.CharField(max_length=255, choices=EMAIL_STATUS_CHOICES, unique=True)

    class Meta:
        db_table = "email-status"
        verbose_name = "Email Status"
        verbose_name_plural = "Email Statuses"

    def __str__(self):
        return self.name


class Mailing(BaseModel):
    sender = models.EmailField(blank=False, null=False)
    recipient = models.EmailField(blank=False, null=False)
    subject = models.TextField(max_length=2000, blank=False, null=False)
    body = models.TextField(max_length=2000, blank=False, null=False)
    status = models.ForeignKey(EmailStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = "mailing"
        verbose_name = "Mailing"

    def __str__(self) -> str:
        return f"""
                From: {self.sender},
                To: {self.recipient},
                Subject: {self.subject}        
                """
