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
    otp = serializers.IntegerField(validators=otp_validate)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ('otp', 'email')





