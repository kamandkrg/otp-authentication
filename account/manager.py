
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(' email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_field):
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_superuser', False)
        extra_field.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_field)

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)
        if (extra_field.get('is_superuser') and extra_field.get('is_staff')) is not True:
            raise ValueError('is_superuser must be True')
        return self._create_user(email, password, **extra_field)
