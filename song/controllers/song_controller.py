from django.shortcuts import render
from song.models.song import Song
from song.models.album import Album

def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        # POST, get the request body parameter and filter pizza
        name = req['name']
        songs = Song.objects.filter(name__contains=name)
    else:
        songs = Song.objects.all()  # get all pizzas
    # put in data dictionary
    data = {
        'songs': songs,
    }
    # render to our html
    return render(request, 'songs.html', context=data)

