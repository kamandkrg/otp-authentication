from django.urls import path

from account.views import VerifyEmailView, SingUpView

urlpatterns = [
    path('email-verify/', VerifyEmailView.as_view(), name='email-verify'),
    path('register/', SingUpView.as_view(), name='register')
]
