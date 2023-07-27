from django.shortcuts import render
from .models import Room
# Create your views here.


# rooms = [
#     {'id':1, 'name':'Python crash course'},
#     {'id':2, 'name':'Javascript crash course'},
#     {'id':3, 'name':'C crash course'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'front/home.html', context)

def room(request, pk):
    room = Room.objects.get(pk=id)
    context = {'room': room}
    return render(request, 'front/room.html', context) 