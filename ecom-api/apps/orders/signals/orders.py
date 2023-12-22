from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from apps.mailing.models import EmailStatus, Mailing
from apps.mailing.scripts.send_mail import init_send_mail
from apps.mailing.templates import ORDER_CREATION_TEMPLATE, ORDER_SUCCESSFUL_EMAIL


def init_mail_to_admin(instance):
    customer_instance = instance.customer
    order_info = (
        customer_instance.first_name + " " + customer_instance.last_name,
        instance.paid_amount,
        customer_instance.address,
        customer_instance.city,
        customer_instance.zip_code,
    )
    admin_mail_template = ORDER_CREATION_TEMPLATE.split(":")
    subject = admin_mail_template[0].strip()
    body = admin_mail_template[1].format(*order_info).strip()
    mail = Mailing.objects.create(
        sender=settings.EMAIL_HOST_USER,
        recipient=settings.ADMIN_RECIEVER_EMAIL,
        subject=subject,
        body=body,
        status=EmailStatus.objects.get(name="PENDING"),
    )
    mail.save()
    result = init_send_mail(
        subject=subject,
        body=body,
        recipient=settings.ADMIN_RECIEVER_EMAIL,
        sender=settings.EMAIL_HOST_USER,
    )
    if result.get("success"):
        mail.status = EmailStatus.objects.get(name="SENT")
        mail.save()
    else:
        mail.status = EmailStatus.objects.get(name="RETRY")
        mail.save()


def init_mail_to_customer(instance):
    recipient_email = instance.customer.email
    customer_mail_template = ORDER_SUCCESSFUL_EMAIL.split(":")
    subject = customer_mail_template[0].strip()
    body = customer_mail_template[1]
    mail = Mailing.objects.create(
        sender=settings.EMAIL_HOST_USER,
        recipient=recipient_email,
        subject=subject,
        body=body,
        status=EmailStatus.objects.get(name="PENDING"),
    )
    mail.save()
    result = init_send_mail(
        subject=subject,
        body=body,
        recipient=recipient_email,
        sender=settings.EMAIL_HOST_USER,
    )
    if result.get("success"):
        mail.status = EmailStatus.objects.get(name="SENT")
        mail.save()
    else:
        mail.status = EmailStatus.objects.get(name="RETRY")
        mail.save()


@receiver(post_save, sender=apps.get_model("orders", "Order"))
def send_order_created_email(sender, instance, created, **kwargs):
    if created:
        init_mail_to_admin(instance)
        init_mail_to_customer(instance)
