# Generated by Django 2.2.5 on 2020-09-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0007_remove_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]