# Generated by Django 3.0.3 on 2020-09-12 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('primaryCategory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, upload_to='products/')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('preview_text', models.TextField(max_length=200, verbose_name='Preview Text')),
                ('detail_text', models.TextField(max_length=1000, verbose_name='Detail Text')),
                ('price', models.FloatField()),
                ('size', models.CharField(choices=[('XXS', 'XXS'), ('XS', 'XS-S'), ('S', 'S'), ('M', 'M'), ('M-L', 'L'), ('XL', 'XL')], max_length=5)),
                ('color', models.CharField(choices=[('Blacks', 'Blacks'), ('Whites', 'Whites'), ('Reds', 'Reds'), ('Greys', 'Greys'), ('Blues', 'Blues'), ('Beige Tones', 'Beige Tones'), ('Greens', 'Greens'), ('Yellows', 'Yellows')], max_length=15)),
                ('label', models.CharField(max_length=40, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionapp.Category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]