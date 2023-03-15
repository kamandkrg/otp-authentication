
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(' phone/email must be set')
        if '@' in username:
            email = self.normalize_email(username)
            user = self.model(email=email, username=username, **extra_fields)
        else:
            user = self.model(phone=username, username=username, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_field):
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_superuser', False)
        extra_field.setdefault('is_staff', False)
        return self._create_user(username, password, **extra_field)

    def create_superuser(self, username, password, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)
        if (extra_field.get('is_superuser') and extra_field.get('is_staff')) is not True:
            raise ValueError('is_superuser must be True')
        return self._create_user(username, password, **extra_field)
