from django.shortcuts import render
from song.models.singer import Singer


def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        singers = Singer.objects.filter(name__contains=name)
    else:
        singers = Singer.objects.all()  
    data = {
        'singers': singers,
    }
    return render(request, 'singers.html', context=data)

