# Generated by Django 4.2 on 2023-06-01 05:48

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0004_alter_cash_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='aes_key',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True),
        ),
    ]
