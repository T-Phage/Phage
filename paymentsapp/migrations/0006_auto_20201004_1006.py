# Generated by Django 2.2.5 on 2020-10-04 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapp', '0005_auto_20201003_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payerdetails',
            name='payer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]