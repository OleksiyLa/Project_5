# Generated by Django 4.2.7 on 2024-01-03 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_status_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderprogress',
            name='managed_by',
        ),
        migrations.RemoveField(
            model_name='orderprogress',
            name='order',
        ),
    ]
