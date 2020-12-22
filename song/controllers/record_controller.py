from django.shortcuts import render
from song.models import Song, Singer, Album


def record(request):
    # get all info here including singers, songs, and albums
    num_songs = Song.objects.all().count()
    num_singers = Singer.objects.all().count()
    num_albums = Album.objects.all().count()
    context = {
        'num_songs': num_songs,
        'num_singers': num_singers,
        'num_albums': num_albums,
    }
    return render(request, 'record.html', context=context)