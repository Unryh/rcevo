# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_newspost_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='new_field',
            field=models.IntegerField(default=0),
        ),
    ]