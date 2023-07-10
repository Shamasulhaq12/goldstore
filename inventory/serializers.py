from rest_framework import serializers
from .models import Account, BalanceReport


class BalanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceReport
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
