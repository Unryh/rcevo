# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime


class News_post(models.Model):
    news_title_picture = models.FileField()
    news_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    news_posting_time = models.DateTimeField(auto_now_add='true')
    news_anotation = models.TextField(max_length=200)
    news_text = models.TextField(max_length=10000)
    news_views_count = models.IntegerField(default=0)
    news_comments_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('main:news_details', kwargs={'slug':self.slug})


class Advanced_user(User):
    avatar = models.FileField(upload_to='media', blank=True)


class Comment_model(models.Model):
    user_nickname = models.ForeignKey(Advanced_user, models.CASCADE,)
    article = models.ForeignKey(News_post, models.CASCADE,)
    parent = models.ForeignKey('self', blank=True, null=True)
    text = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add='true')

    def __unicode__(self):
        return self.text[:30]

    def get_user_avatar(self):
        a = Advanced_user.objects.get(username=self.user_nickname)
        return a.avatar.url


class Pictures_for_news(models.Model):
    parent_news = models.ForeignKey(News_post, models.CASCADE,)
    picture = models.FileField(default='media')
