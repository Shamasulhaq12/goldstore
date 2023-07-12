from rest_framework import serializers
from .models import Account, BalanceReport, GoldPrice


class GoldPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldPrice
        fields = "__all__"


class BalanceReportSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    account_name  = serializers.CharField(source='account.name', read_only=True)

    def get_balance(self, obj):
        return self.context['request'].user.balance

    class Meta:
        model = BalanceReport
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
