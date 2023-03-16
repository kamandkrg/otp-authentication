from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from lib.validations import otp_validate

User = get_user_model()


class RegisterPhoneSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField(validators=[otp_validate], write_only=True)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('phone', 'password', 'otp')

    def validate(self, attrs):
        otp_cache = cache.get(attrs['phone'])
        if otp_cache != attrs['otp']:
            raise ValidationError('code is wrong')

        return attrs

    def save(self, **kwargs):

        validated_data = {**self.validated_data, **kwargs}
        password = validated_data.pop('password1')
        validated_data.pop('otp')
        user = User.objects.create_user(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class SendSMSSerializer(serializers.Serializer):
    phone = serializers.CharField(write_only=True)


class RegisterEmailSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField(validators=[otp_validate], write_only=True)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password', 'otp')

    def validate(self, attrs):
        otp_cache = cache.get(attrs['email'])
        if otp_cache != attrs['otp']:
            raise ValidationError('code is wrong')

        return attrs

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        password = validated_data.pop('password1')
        validated_data.pop('otp')
        user = User.objects.create_user(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class SendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)















