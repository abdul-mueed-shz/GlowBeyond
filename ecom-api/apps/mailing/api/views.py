from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView


class SendSimpleEmail(APIView):
    def post(self, request):
        response = Response()

        email = request.data.get("email")
        if not email:
            response.data = {"error": "Email is required"}
            response.status_code = 400
            return response

        try:
            message = "Dear Anon, I hope this email finds you well."
            send_mail(
                "Greetings",
                message,
                "abdul.mueed.shz.dev@gmail.com",
                [email],
                fail_silently=False,
            )
            return response

        except Exception as e:
            response.data = {"error": str(e)}
            response.status_code = 500
            return response
