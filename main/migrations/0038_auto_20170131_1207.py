# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20170131_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='news_comments_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news_post',
            name='news_views_count',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
