# Generated by Django 4.1.7 on 2023-06-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=1000)),
                ('Email', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=100)),
                ('Address_line_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('zip', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=12)),
            ],
        ),
    ]
