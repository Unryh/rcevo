# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20170121_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_db',
            name='test_user_nickname',
        ),
        migrations.DeleteModel(
            name='Test_db',
        ),
    ]
