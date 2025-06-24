from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_author', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_author', 'is_staff', 'is_superuser')

    fieldsets = UserAdmin.fieldsets + (
        ('Thông tin bổ sung', {
            'fields': ('avatar', 'bio', 'date_of_birth', 'is_author')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Thông tin bổ sung', {
            'fields': ('avatar', 'bio', 'date_of_birth', 'is_author')
        }),
    )