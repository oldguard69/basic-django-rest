# Generated by Django 3.2.6 on 2021-08-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210823_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
