# Generated by Django 3.2.4 on 2021-06-05 10:20

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название страны')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Цвет колонки')),
                ('population', models.PositiveBigIntegerField(verbose_name='Численность населения')),
            ],
        ),
    ]
