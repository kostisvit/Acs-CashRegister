# Generated by Django 4.2 on 2024-04-19 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0018_cash_pos_connect'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfile',
            options={'permissions': [('upload_file', 'Can upload file (upload-file)')], 'verbose_name': 'Αρχεία', 'verbose_name_plural': 'Αρχεία'},
        ),
    ]
