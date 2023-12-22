from django.conf import settings
from django.core.mail import send_mail


def init_send_mail(
    subject,
    body,
    recipient,
    sender=settings.EMAIL_HOST_USER,
):
    try:
        send_mail(
            subject,
            body,
            sender,
            [recipient],
            fail_silently=False,
        )
        return {"success": True, "message": "Email sent successfully"}

    except Exception as e:
        return {"success": False, "error": f"Failed to send email: {str(e)}"}
