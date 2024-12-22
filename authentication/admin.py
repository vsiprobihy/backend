from django.contrib import admin

from authentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName', 'role', 'isActive')
    list_filter = ('role', 'isActive')
    search_fields = ('email', 'firstName', 'lastName')
