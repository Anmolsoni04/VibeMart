# Generated by Django 4.1.7 on 2023-06-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone_number',
            field=models.CharField(default='blank', max_length=12),
        ),
    ]
