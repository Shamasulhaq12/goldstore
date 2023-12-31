# Generated by Django 4.2.3 on 2023-07-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_balancereport_cash_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancereport',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='cash_in',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='cash_out',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='gold',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='payable',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='rati',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='balancereport',
            name='receivable',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='goldprice',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
