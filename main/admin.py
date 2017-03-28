# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NewsPost, Advanced_user, Comment_model, Picture_for_news


class For_pictures(admin.ModelAdmin):
    list_display = ('news_id', 'picture')


class Connection_with_picture(admin.TabularInline):
    model = Picture_for_news


class News_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posting_time')
    list_filter = ['slug']
    search_fields = ['title']
    fields = ('title', 'slug', 'annotation', 'text', 'title_picture', )

    inlines = [
        Connection_with_picture,
    ]


admin.site.register(NewsPost, News_postAdmin)
admin.site.register(Advanced_user)
admin.site.register(Comment_model)
admin.site.register(Picture_for_news, For_pictures)

