# Generated by Django 4.2.7 on 2024-01-03 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0002_order_original_bag_order_stripe_pid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(blank=True, null=True)),
                ('is_being_cooked', models.BooleanField(default=False)),
                ('start_cooking_at', models.DateTimeField(blank=True, null=True)),
                ('is_being_prepared', models.BooleanField(default=False)),
                ('start_preparing_at', models.DateTimeField(blank=True, null=True)),
                ('is_being_delivered', models.BooleanField(default=False)),
                ('start_delivering_at', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('managed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
