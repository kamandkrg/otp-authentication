from django.urls import path

from account.views import RegisterPhoneAPIView, SendSMSAPIView, RegisterEmailAPIView, SendEmailAPIView

urlpatterns = [
    path('api/phone-register/', RegisterPhoneAPIView.as_view(), name='phone-register'),
    path('api/send-sms/', SendSMSAPIView.as_view(), name='send-sms'),
    path('api/email-register/', RegisterEmailAPIView.as_view(), name='email-register'),
    path('api/send-email/', SendEmailAPIView.as_view(), name='send-email'),
]
