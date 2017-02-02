from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Model_for_tracks(models.Model):
    track_name = models.CharField(max_length=100)
    track_title_picture = models.FileField(default='media')
    track_type = models.CharField(max_length=100)
    track_adress = models.CharField(max_length=200)
    track_information = models.TextField(max_length=10000)
    track_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.track_name

    def get_absolute_url(self):
        return reverse('track_map:track_index')


class Pictures_for_track(models.Model):
    parent_track = models.ForeignKey(Model_for_tracks, models.CASCADE,)
    picture = models.FileField(default='media')
