# Generated by Django 4.2 on 2023-10-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0016_rename_uuid_uploadfile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='voucher',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
