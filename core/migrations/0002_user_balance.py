# Generated by Django 4.2.3 on 2023-07-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
    ]