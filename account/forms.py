from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class NewUserForm(forms.ModelForm):
    password1 = forms.CharField(label='password')
    password2 = forms.CharField(label='password confirmation')

    class Meta:
        mode = User
        fields = ('email', )

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password don\'t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'first_name', 'last_name', 'age', 'sex', 'national_code', 'job', 'birthday', 'is_active', 'is_seller', 'is_staff', 'is_superuser')

    def clean_password(self):
        return self.initial['password']


