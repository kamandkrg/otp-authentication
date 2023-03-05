from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from account.forms import NewUserForm, UserChangeForm

User = get_user_model()


class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = NewUserForm
    list_display = ('id', 'email', 'phone', 'username', 'first_name', 'last_name',
                    'age', 'sex', 'national_code', 'job', 'birthday', 'is_active',
                    'is_seller', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'is_staff', 'is_superuser', 'is_seller', 'password', 'is_active')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'age', 'sex', 'email', 'birthday', 'job')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_seller', 'is_staff', 'is_superuser', 'is_active',
                           'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'age', 'sex', 'email', 'birthday', 'job')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'username', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, AccountAdmin)
