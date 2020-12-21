from django.shortcuts import render
from song.models.song import Song

def record(request):
    # get all info here including singers, songs, and albums
    songs = Song.objects.all()
    data = {
        'songs': songs,
    }
    return render(request, 'record.html', context=data)