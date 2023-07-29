from django.shortcuts import render, redirect
from .models import Room

from .forms import RoomForm
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
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'front/room.html', context) 

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'front/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    content = {'form': form}
    return render(request, 'front/room_form.html', content)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'front/delete_form.html', {'obj': room})