from django.shortcuts import render
# we import the models here, usually only one model
from song.models.song import Song

def index(request):
        songs = Song.objects.all() # get all pizzas
# put in data dictionary
        data = {
        'songs': songs,
        }
        return render(request, 'songs.html', context=data)