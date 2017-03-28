from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class TypesDB(models.Model):
    track_type = models.CharField(primary_key=True, max_length=100)

    def __unicode__(self):
        return self.track_type


class Track(models.Model):
    name = models.CharField(max_length=100)
    title_picture = models.FileField(default='media')
    type = models.ForeignKey(TypesDB, models.CASCADE, default='None')
    address = models.CharField(max_length=200)
    information = models.TextField(max_length=10000)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('track_map:track_index')


class TypesOfTrack(models.Model):
    track_id = models.ForeignKey(Track, null=True)
    track_type = models.ForeignKey(TypesDB, models.CASCADE, )


class PictureForTrack(models.Model):
    track_id = models.ForeignKey(Track, models.CASCADE, )
    picture = models.FileField(default='media')

