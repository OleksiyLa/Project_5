# Generated by Django 4.2.7 on 2024-01-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='name',
            field=models.CharField(max_length=100, null=False),
        ),
    ]