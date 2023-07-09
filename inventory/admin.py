from django.contrib import admin

# Register your models here.

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'receivable', 'payable', 'balance', 'rati', 'gold',
                    'cash_in', 'cash_out', 'cash_balance', 'created_at', 'updated_at')
    ordering = ('name', 'receivable', 'payable', 'balance', 'rati', 'gold',
                'cash_in', 'cash_out', 'cash_balance', 'created_at', 'updated_at')
