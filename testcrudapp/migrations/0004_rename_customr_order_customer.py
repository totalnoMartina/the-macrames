# Generated by Django 3.2 on 2022-08-17 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcrudapp', '0003_auto_20220817_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customr',
            new_name='customer',
        ),
    ]
