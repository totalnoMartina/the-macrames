# Generated by Django 3.2 on 2022-08-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcrudapp', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testcrudapp.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testcrudapp.product'),
        ),
    ]
