# Generated by Django 4.2 on 2024-09-04 05:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='codigo',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='supervisores',
            name='codigo',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='codigo',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
