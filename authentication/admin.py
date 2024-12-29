from django.contrib import admin

from authentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'firstName', 'lastName')
