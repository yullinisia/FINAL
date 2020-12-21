from django.contrib import admin
from song.models.singer import Singer
from song.models.song import Song
from song.models.album import Album


admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)
# Register your models here.
