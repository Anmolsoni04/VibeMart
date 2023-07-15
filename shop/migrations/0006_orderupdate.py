# Generated by Django 4.1.7 on 2023-06-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_orders_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=2000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
