from django.core.mail import send_mail


def send_mail_to_admin():
    receiver = "abdulmueedshahbaz@gmail.com"
    try:
        message = "Dear Anon, I hope this email finds you well."
        send_mail(
            "Greetings",
            message,
            "abdul.mueed.shz.dev@gmail.com",
            [receiver],
            fail_silently=False,
        )
        return {"success": True, "message": "Email sent successfully"}

    except Exception as e:
        return {"success": False, "error": f"Failed to send email: {str(e)}"}
