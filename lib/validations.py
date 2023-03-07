from django.core.exceptions import ValidationError


def otp_validate(value):
    if not (1000 > value > 9999):
        raise ValidationError('otp must be between 1000-9999')



