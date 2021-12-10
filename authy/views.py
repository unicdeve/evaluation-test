from django.contrib.auth import authenticate, get_user_model
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .permissions import *
from .serializers import UserSerializer

UserModel = get_user_model()


class LoginViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        user = authenticate(request, **request.data)

        if user:
            (token, _) = Token.objects.get_or_create(user=user)

            data = {"token": token.key,
                    "id": user.id, 'email': user.email}

            return Response(data)

        return Response(["Wrong email/password."], status=status.HTTP_401_UNAUTHORIZED)


class LogoutViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        try:
            Token.objects.get(user=request.user).delete()
        except Token.DoesNotExist:
            pass

        return Response()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # user_email = request.data.get('email')

            return Response({"token": user.auth_token.key, "id": user.id, "email": user.email}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


