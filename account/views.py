from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from account.serializers import CreateUserSerializers, VerifyEmailSerializer

User = get_user_model()


class SingUpView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreateUserSerializers
    queryset = User.bojects.all()


class VerifyEmailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        try:
            return User.objects.get(self.request.user.pk)
        except User.DoesNotExist:
            raise User

    def get(self, request):
        pass

    def post(self, request):
        pass



