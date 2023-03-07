from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from lib.validations import otp_validate

User = get_user_model()


class CreateUserSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(label='Password', write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1')

    def save(self, **kwargs):

        validated_data = {**self.validated_data, **kwargs}
        password = validated_data.pop('password1')
        user = User.objects.create_user(
            **validated_data
        )
        user.set_password(password)
        user.is_staff = False
        user.save()
        return user


class VerifyEmailSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField(validators=otp_validate, write_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ('otp', 'email')

    def validate_otp(self, attr):
        if attr['otp'] != self.context['request'].user.otp:
            raise ValidationError('token is wrong')
        return attr

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        instance.is_active = True
        instance.save()
        return instance




