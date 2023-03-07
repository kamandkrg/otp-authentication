import random

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import Http404

User = get_user_model()


@shared_task
def send_email(email, token):
    email_from = settings.EMAIL_HOST_USER
    send_mail('Verify Email', f'your token is: {token}', email_from, [email])

