# Generated by Django 4.2 on 2024-02-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0017_cash_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='pos_connect',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
