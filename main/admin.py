# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import News_post, Advanced_user, Comment_model




class News_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('news_title',)}
    list_display = ('news_title', 'news_posting_time')
    list_filter = ['slug']
    search_fields = ['news_title']

admin.site.register(News_post,News_postAdmin)
#admin.site.register(Site_users)
admin.site.register(Advanced_user)
#admin.site.register(Test_db)
admin.site.register(Comment_model)
