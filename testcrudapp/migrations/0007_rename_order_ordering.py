# Generated by Django 3.2 on 2022-08-17 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcrudapp', '0006_auto_20220817_1626'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Ordering',
        ),
    ]
