# Generated by Django 4.2 on 2023-09-11 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0003_cash_file_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cash',
            name='file_url',
        ),
    ]
