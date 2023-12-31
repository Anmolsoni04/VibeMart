# Generated by Django 4.1.7 on 2023-07-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_done_amount',
            field=models.CharField(default='blank', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(default='blank', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_signature',
            field=models.CharField(default='blank', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_order_id',
            field=models.CharField(default='blank', max_length=100),
        ),
    ]
