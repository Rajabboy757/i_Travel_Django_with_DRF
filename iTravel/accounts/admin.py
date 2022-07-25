from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'email', 'birth_day', 'birth_month', 'birth_year', 'phone', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('birth_day', 'birth_month', 'birth_year',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('birth_day', 'birth_month', 'birth_year',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
