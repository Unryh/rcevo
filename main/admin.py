# -*- coding: utf-8 -*-
from django.contrib import admin
from models.models import NewsPost, AdvancedUser, CommentModel, PictureForNews


class ForPictures(admin.ModelAdmin):
    list_display = ('news', 'picture')


class ConnectionWithPicture(admin.TabularInline):
    model = PictureForNews


class NewsPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posting_time')
    list_filter = ['slug']
    search_fields = ['title']
    fields = ('title', 'slug', 'annotation', 'text', 'title_picture')

    inlines = [
        ConnectionWithPicture,
    ]


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(AdvancedUser)
admin.site.register(CommentModel)
admin.site.register(PictureForNews, ForPictures)

