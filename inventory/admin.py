from django.contrib import admin

# Register your models here.

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )
