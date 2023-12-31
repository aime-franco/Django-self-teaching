from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RoomForm
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesn\'t exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password is invalid')
    content = {}        
    return render(request, 'front/login_register.html', content)

def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occurred during the registeration')    
  
    return render(request, 'front/register.html', {'form': form})

@login_required(login_url='login')
def home(request):
    q = request.GET.get('p') if request.GET.get('p') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
    Q(name__icontains=q)
    )
  
    topics = Topic.objects.all() 
    count_room = rooms.count() # count the number of rooms the topic
    context = {'rooms': rooms, 'topics': topics, 'count_room': count_room,}
    return render(request, 'front/home.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages}
    return render(request, 'front/room.html', context) 

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'front/room_form.html', context)

@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'front/delete_form.html', {'obj': room})