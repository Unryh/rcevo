# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


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

# class Site_users(models.Model):
#    avatar = models.FileField(upload_to='media', null=True, blank=True)
#    username = models.CharField(max_length=50)
#    email = models.EmailField(max_length=254)
#    password = models.CharField(max_length=50)


class Advanced_user(User):
    #testirovanit = models.CharField(max_length=100, blank=True)
    avatar = models.FileField(upload_to='media', blank = True)


class Comment_model(models.Model):
    user_nickname = models.ForeignKey(Advanced_user, models.CASCADE,)
    parent_object = models.ForeignKey(News_post, models.CASCADE,)
    text = models.TextField(max_length=1000)


class Test_db(models.Model):
    test_user_nickname = models.ForeignKey(Advanced_user, models.CASCADE, default='common_user')
    comment_text = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.comment_text

