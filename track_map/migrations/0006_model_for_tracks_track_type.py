# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track_map', '0005_remove_model_for_tracks_track_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_for_tracks',
            name='track_type',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='track_map.Types_db'),
        ),
    ]
