from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("login", "email")
    list_display = (
        "__str__",
        "is_staff",
        "is_active",
        "is_verified",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "is_verified",
    )
