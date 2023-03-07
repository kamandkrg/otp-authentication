from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True, null=True, blank=True)
    phone = models.CharField(null=True, unique=True, blank=True, max_length=13)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    verify_email = models.BooleanField(default=False)
    otp = models.IntegerField(null=True, blank=True)
    national_code = models.PositiveBigIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
