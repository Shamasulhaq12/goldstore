from rest_framework import serializers
from .models import Account, BalanceReport, GoldPrice


class GoldPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldPrice
        fields = "__all__"


class BalanceReportSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    account_name = serializers.CharField(source='account.name', read_only=True)
    total_payable = serializers.SerializerMethodField()
    total_receivable = serializers.SerializerMethodField()

    def get_payable(self, obj):
        try:
            return obj.total_payable
        except:
            return 0

    def get_receivable(self, obj):
        try:
            return obj.total_receivable
        except:
            return 0

    def get_balance(self, obj):
        return self.context['request'].user.balance

    class Meta:
        model = BalanceReport
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    balance_report = serializers.SerializerMethodField()

    def get_balance_report(self, obj):
        return BalanceReportSerializer(obj.balance_report.last(), context={'request': self.context['request']}).data

    class Meta:
        model = Account
        fields = "__all__"
