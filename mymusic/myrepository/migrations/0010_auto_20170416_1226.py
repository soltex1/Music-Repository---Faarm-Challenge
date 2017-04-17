# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrepository', '0009_auto_20170416_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='album',
        ),
        migrations.AddField(
            model_name='artist',
            name='album',
            field=models.ManyToManyField(to='myrepository.Album'),
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ManyToManyField(to='myrepository.Album'),
        ),
    ]