import random

from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegisterPhoneSerializer, SendSMSSerializer, SendEmailSerializer, RegisterEmailSerializer
from account.tasks import send_email_task, send_sms_task

User = get_user_model()


class RegisterPhoneAPIView(CreateAPIView):
    serializer_class = RegisterPhoneSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )


class SendSMSAPIView(APIView):

    def post(self, request):
        phone_serializer = SendSMSSerializer(data=request.data)
        if phone_serializer.is_valid():
            token = random.randint(1000, 9999)
            phone = request.data['phone']
            print(phone)
            cache.set(phone, token)
            send_sms_task.delay(phone, token)
            return Response({'message': 'sent code to phone number'})
        return Response({'message': phone_serializer.errors})


class RegisterEmailAPIView(CreateAPIView):
    serializer_class = RegisterEmailSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )


class SendEmailAPIView(APIView):

    def post(self, request):
        email_serializer = SendEmailSerializer(data=request.data)
        if email_serializer.is_valid():
            token = random.randint(1000, 9999)
            email = request.data['email']
            cache.set(email, token)
            send_email_task.delay(email, token)
            return Response({'message': 'sent code to phone number'})
        return Response({'message': email_serializer.errors})

