# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klony', '0004_auto_20170201_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acers',
            name='new_image_bark',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='acers',
            name='new_image_leaf',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='acers',
            name='new_image_tree',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]