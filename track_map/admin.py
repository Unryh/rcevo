# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Model_for_tracks, Pictures_for_track, Types_db, \
    Types_of_tracks


class Connection_with_track_types(admin.TabularInline):
    model = Types_of_tracks


class For_pictures(admin.ModelAdmin):
    list_display = ('parent_track', 'picture')


class Connection_with_pictures(admin.TabularInline):
    model = Pictures_for_track


class Model_for_tracks_admin(admin.ModelAdmin):
    fields = ('track_name', 'track_title_picture', 'track_adress',
              'track_information')
    inlines = [
        Connection_with_pictures,
        Connection_with_track_types,
    ]


admin.site.register(Types_db)
admin.site.register(Model_for_tracks, Model_for_tracks_admin)
admin.site.register(Pictures_for_track, For_pictures)
admin.site.register(Types_of_tracks)


