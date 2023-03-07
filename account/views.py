import random

from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import CreateUserSerializers, VerifyEmailSerializer
from account.tasks import send_email

User = get_user_model()


class SingUpView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreateUserSerializers
    queryset = User.objects.all()


class VerifyEmailView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = VerifyEmailSerializer

    def get(self, request, *args, **kwargs):
        serializer = VerifyEmailSerializer(request.user)
        token = random.randint(1000, 9999)
        request.user.otp = token
        request.user.save()
        send_email.apply_async([request.user.email, token])
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = VerifyEmailSerializer(request.user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response('user is active')
        return Response(serializer.errors)



