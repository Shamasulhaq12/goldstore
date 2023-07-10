from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GoldPrice(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)


class BalanceReport(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='balance_report')
    gold_price = models.ForeignKey(
        GoldPrice, on_delete=models.CASCADE, related_name='balance_gold_price')
    receivable = models.DecimalField(max_digits=10, decimal_places=5)
    payable = models.DecimalField(max_digits=10, decimal_places=5)
    balance = models.DecimalField(max_digits=10, decimal_places=5)
    rati = models.DecimalField(max_digits=10, decimal_places=5)
    gold = models.DecimalField(max_digits=10, decimal_places=5)
    cash_in = models.DecimalField(max_digits=10, decimal_places=5)
    cash_out = models.DecimalField(max_digits=10, decimal_places=5)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)
