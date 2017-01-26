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
    news_picture = models.FileField(default='media')
    news_posting_time = models.DateTimeField(auto_now_add='true')
    news_anotation = models.TextField(max_length=200)
    news_text = models.TextField(max_length=10000)
    news_views_count = models.CharField(max_length=10)
    news_comments_count = models.CharField(max_length=10)

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

    def avatar_print(self):
        a = Advanced_user.objects.get(username=self.user_nickname)
        return a.avatar.url

# class Test_db(models.Model):
#     super_test_user_nickname = models.TextField(max_length=1000, default='supertest')
#     test_user_nickname = models.ForeignKey(Advanced_user, models.CASCADE, default='2') #pk2 - unryh, pk4 - anna
#     comment_text = models.TextField(max_length=1000)
#
#     def __unicode__(self):
#         return self.comment_text

