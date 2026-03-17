from django.shortcuts import render, redirect
from .models import GameSession
from .game import generate_map
# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def new_game(request):
    grid = generate_map()
    session = GameSession.objects.create(
        player_x = 0,
        player_y = 0,
        map_data = {'grid': grid},
    )

    request.session['game_id'] = session.id    
    return redirect("map")    

def map_view(request):
    session = GameSession.objects.get(id= request.session['game_id'])
    grid = session.map_data['grid']
    return render(request,
                   "home/map.html", {'session': session, 'grid': grid,})

def move(request, direction):
    session = GameSession.objects.get(id = request.session['game_id'])
    if direction == 'north': session.player_y -= 1
    if direction == 'south': session.player_y += 1
    if direction == 'west': session.player_x -= 1
    if direction == 'east': session.player_x += 1

    session.save()
    return redirect("map")

def combat(request):
    session = GameSession.objects.get(id = request.session['game_id'])
    return render(request, "home/combat.html", {'session': session})

def attack(request):
    return render("combat")

