from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.views import APIView
import jwt

from django.contrib.auth.models import User

from apps.user.api.serializers import RegisterSerializer, UserSerializer, TokenSerializer


# Create your views here.
class AuthDetails(APIView):
    def check_required_fields(self, payload):
        if payload.get('first_name') and payload.get('last_name') and payload.get('email') and payload.get('exp'):
            return {
                'email': payload.get('email'),
                'first_name': payload.get('first_name'),
                'last_name': payload.get('last_name'),
                'expiry': payload.get('exp')
            }
        return False

    def save_auth_token(self, token_data):
        try:
            serializer = TokenSerializer(data=token_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            raise ValidationError("Invalid token data")

    def get(self, request):
        auth_token = request.query_params.get('auth_token', None)
        if not auth_token:
            raise AuthenticationFailed("No authentication token found")

        response = Response()

        try:
            payload = jwt.decode(auth_token, 'secret', algorithms=['HS256'])

            registration_data = self.check_required_fields(payload)
            if not registration_data:
                raise AuthenticationFailed("Malformed authentication token")

            token_expiry = registration_data.pop('expiry')
            token_data = {
                'token': auth_token,
                'expiry': token_expiry,
            }

            response.set_cookie(key='auth_token', value=auth_token, httponly=True)
            data = {'auth_token': auth_token, 'expiry': token_expiry, }

            user = User.objects.filter(email=registration_data.get('email'))
            if not len(user):
                serializer = RegisterSerializer(
                    data=registration_data
                )
                serializer.is_valid(raise_exception=True)
                user = serializer.save()

                token_data['user'] = user.id
                self.save_auth_token(token_data)

                data['user_information'] = serializer.data
                response.data = data

                return response

            serializer = UserSerializer(user[0])

            token_data['user'] = user[0].id
            self.save_auth_token(token_data)

            data["user_information"] = serializer.data
            response.data = data

            return response

        except jwt.ExpiredSignatureError:
            response.delete_cookie(key='auth_token')
            raise AuthenticationFailed("Unauthenticated")
