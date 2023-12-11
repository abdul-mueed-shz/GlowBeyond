from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from apps.mailing.scripts.send_mail import send_mail_to_admin


@receiver(post_save, sender=apps.get_model("orders", "Order"))
def send_order_created_email(sender, instance, **kwargs):
    result = send_mail_to_admin()

    if result.get("success"):
        print("Email sent successfully for order creation.")
    else:
        print(f"Failed to send email. Error: {result.get('error')}")
