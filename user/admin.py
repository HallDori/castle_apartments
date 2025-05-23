
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Expose custom User in Django admin."""

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Profile",
            {"fields": ("profile_image",)},
        ),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets
    list_display = ("username", "email", "first_name", "last_name", "is_staff")