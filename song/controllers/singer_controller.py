from django.shortcuts import render
from song.models.singer import Singer
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import SingerForm

def index(request):
    singers = Singer.objects.all()  
    data = {
        'singers': singers,
    }
    return render(request, 'singers.html', context=data)

def add_singer(request):
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('singers'))
    else:
        form = SingerForm()

    context = {
        'form': form
    }
    return render(request, 'singer_form.html', context=context)

def edit_singer(request, singer_id):
    if request.method == 'POST':
        singer = Singer.objects.get(pk=singer_id)
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('singers'))
    else:
        singer = Singer.objects.get(pk=singer_id)
        fields = model_to_dict(singer)
        form = SingerForm(initial=fields, instance=singer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'singer_form.html', context=context)


def delete_singer(request, singer_id):
    singer = Singer.objects.get(pk=singer_id)
    if request.method == 'POST':
        singer.delete()
        return HttpResponseRedirect(reverse('singers'))
    context = {
        'singer': singer
    }
    return render(request, 'singer_delete_form.html', context=context)
