# Generated by Django 4.2 on 2023-09-20 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tameiaki', '0008_remove_cash_file_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tameiaki.cash'),
        ),
    ]
