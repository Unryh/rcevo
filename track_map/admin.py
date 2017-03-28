# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Track, PictureForTrack, TypesDB, TypesOfTrack


class ConnectionWithTrackTypes(admin.TabularInline):
    model = TypesOfTrack


class ForPictures(admin.ModelAdmin):
    list_display = ('track_id', 'picture')


class ConnectionWithPictures(admin.TabularInline):
    model = PictureForTrack


class TracksAdmin(admin.ModelAdmin):
    fields = ('name', 'title_picture', 'address',
              'information')
    inlines = [
        ConnectionWithPictures,
        ConnectionWithTrackTypes,
    ]

class TypesOfTrackAdmin(admin.ModelAdmin):
    list_display = ('track_id', 'track_type')


admin.site.register(TypesDB)
admin.site.register(Track, TracksAdmin)
admin.site.register(PictureForTrack, ForPictures)
admin.site.register(TypesOfTrack, TypesOfTrackAdmin)


