# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20170328_0956'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News_post',
            new_name='NewsPost',
        ),
    ]
