# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20161128_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_users',
            name='avatar_test',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
