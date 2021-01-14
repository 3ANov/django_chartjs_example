# Generated by Django 3.1.5 on 2021-01-14 10:27

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('population', models.PositiveBigIntegerField()),
            ],
        ),
    ]
