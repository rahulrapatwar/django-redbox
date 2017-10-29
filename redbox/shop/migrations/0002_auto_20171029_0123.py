# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='game_pics'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='movie_pics'),
        ),
    ]
