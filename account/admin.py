from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from account.forms import NewUserForm, UserChangeForm

User = get_user_model()


class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = NewUserForm
    list_display = ('id', 'email', 'phone', 'username', 'first_name', 'last_name',
                    'is_active', 'verify_email',
                    'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'is_staff', 'is_superuser', 'verify_email', 'password', 'is_active')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'email')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_seller', 'is_staff', 'is_superuser', 'is_active', 'verify_email',
                           'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'email')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'username', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, AccountAdmin)
