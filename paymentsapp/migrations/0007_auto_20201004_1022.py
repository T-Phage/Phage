# Generated by Django 2.2.5 on 2020-10-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapp', '0006_auto_20201004_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='payerdetails',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='payerdetails',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payerdetails',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
