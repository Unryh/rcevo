# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    title_picture = models.FileField()
    slug = models.SlugField(max_length=200)
    posting_time = models.DateTimeField(auto_now_add='true')
    annotation = models.TextField(max_length=200)
    text = models.TextField(max_length=10000)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:news_details', kwargs={'slug':self.slug})


class Advanced_user(User):
    avatar = models.FileField(upload_to='media', blank=True,
                              default='/home/albert/IMG_958.JPG')


class Comment_model(models.Model):
    user_nickname = models.ForeignKey(Advanced_user, models.CASCADE,)
    article = models.ForeignKey(NewsPost, models.CASCADE, )
    # parent = models.ForeignKey('self', blank=True, null=True)
    text = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add='true')

    def __unicode__(self):
        return self.text[:30]

    def get_user_avatar(self):
        a = Advanced_user.objects.get(username=self.user_nickname)
        return a.avatar.url


class Picture_for_news(models.Model):
    news_id = models.ForeignKey(NewsPost, models.CASCADE, )
    picture = models.FileField(default='media')
