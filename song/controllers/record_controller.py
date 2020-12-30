from django.shortcuts import render
from song.models import Song, Singer, Album, Producer, Genre

def record(request):
    # we check the session with key ‘num_visits’, if doesn’t exist we set to 1
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1  # add everytime we reload
    # get all info here including authors, books, and genres
    num_songs = Song.objects.all().count()
    num_singers = Singer.objects.all().count()
    num_albums = Album.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_producers = Producer.objects.all().count()
    # pass num_visits as the context to display it on the html
    context = {
        'num_songs': num_songs,
        'num_singers': num_singers,
        'num_albums': num_albums,
        'num_genres' : num_genres,
        'num_producers' : num_producers,
        'total_visit': num_visits,
    }
    return render(request, 'record/record.html', context=context)