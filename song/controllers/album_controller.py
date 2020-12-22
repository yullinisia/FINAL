from django.shortcuts import render
from song.models.album import Album
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import AlbumForm

def index(request):
    albums = Album.objects.all()
    data = {
        'albums': albums,
    }
    return render(request, 'albums.html', data)

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('albums'))
    else:
        form = AlbumForm()

    context = {
        'form': form
    }
    return render(request, 'album_form.html', context=context)

def edit_album(request, album_id):
    if request.method == 'POST':
        album = Album.objects.get(pk=album_id)
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))
    else:
        album = Album.objects.get(pk=album_id)
        fields = model_to_dict(album)
        form = AlbumForm(initial=fields, instance=album)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'album_form.html', context=context)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        album.delete()
        return HttpResponseRedirect(reverse('albums'))
    context = {
        'album': album
    }
    return render(request, 'album_delete_form.html', context=context)
