from django.shortcuts import render
from song.models import Song, Singer, Album
from django.contrib.auth.decorators import login_required
@login_required



def record(request):
    # we check the session with key ‘num_visits’, if doesn’t exist we set to 1
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1  # add everytime we reload
    # get all info here including authors, books, and genres
    num_songs = Song.objects.all().count()
    num_singers = Singer.objects.all().count()
    num_albums = Album.objects.all().count()
    # pass num_visits as the context to display it on the html
    context = {
        'num_songs': num_songs,
        'num_singers': num_singers,
        'num_albums': num_albums,
        'total_visit': num_visits,
    }
    return render(request, 'record.html', context=context)