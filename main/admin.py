# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import News_post, Advanced_user, Comment_model, Pictures_for_news


class For_pictures(admin.ModelAdmin):
    list_display = ('parent_news', 'picture')


class Connection_with_pictures(admin.TabularInline):
    model = Pictures_for_news


class News_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('news_title',)}
    list_display = ('news_title', 'news_posting_time')
    list_filter = ['slug']
    search_fields = ['news_title']
    fields = ('news_title', 'slug', 'news_anotation', 'news_text', 'news_title_picture', )

    inlines = [
        Connection_with_pictures,
    ]


admin.site.register(News_post, News_postAdmin)
admin.site.register(Advanced_user)
admin.site.register(Comment_model)
admin.site.register(Pictures_for_news, For_pictures)

