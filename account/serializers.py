from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class CreateUserSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(label='Password', write_only=True)
    password2 = serializers.CharField(label='Password confirmation', write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username',
                  'age', 'sex', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise ValidationError('password is not mach')
        return attrs

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


class VerifyEmail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('otp', )





