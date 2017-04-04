# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .mixins import CreatedModifiedMixin
from .managers import MainManager
from .managers import CommentManager


class NewsPost(CreatedModifiedMixin, models.Model):
    title = models.CharField(max_length=100)
    title_picture = models.FileField()
    slug = models.SlugField(max_length=200)
    posting_time = models.DateTimeField(auto_now_add='true')
    annotation = models.TextField(max_length=200)
    text = models.TextField(max_length=10000)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    objects = MainManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:news_details', kwargs={'slug': self.slug})


class AdvancedUser(User):
    avatar = models.FileField(upload_to='media', blank=True,
                              default='/home/albert/IMG_958.JPG')


class CommentModel(models.Model):
    user_nickname = models.ForeignKey(AdvancedUser, models.CASCADE, )
    news = models.ForeignKey(NewsPost, models.CASCADE, )
    # parent = models.ForeignKey('self', blank=True, null=True)
    text = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add='true')

    objects = CommentManager()

    def __unicode__(self):
        return self.text[:30]

    def get_user_avatar(self):
        a = AdvancedUser.objects.get(username=self.user_nickname)
        return a.avatar.url


class PictureForNews(models.Model):
    news = models.ForeignKey(NewsPost, models.CASCADE, )
    picture = models.FileField(default='media')
