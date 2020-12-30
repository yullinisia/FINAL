from django.db import models
from song.models.singer import Singer
from song.models.album import Album
from song.models.genre import Genre
from song.models.producer import Producer

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True)
    album = models.ManyToManyField(Album)
    genre = models.ManyToManyField(Genre)
    producer = models.OneToOneField(Producer, on_delete=models.CASCADE, null=True)
    date_published = models.DateField(null=True, blank=True)
    
    class Meta:
        app_label = 'song'
        
    def __str__(self):
        return f'{self.title}'

