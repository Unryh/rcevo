# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track_map', '0006_model_for_tracks_track_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types_of_tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_map.Model_for_tracks')),
                ('track_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_map.Types_db')),
            ],
        ),
    ]