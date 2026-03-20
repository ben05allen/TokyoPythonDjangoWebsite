import random

#Get into the station in time.
#Pyscript #Pyodide

def generate_map(width = 8, height = 8):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() > 0.3:
                grid[y][x] = 1

    grid[0][0] = 1
    return grid


class Player:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.level = 1
        self.xp = 0
        self.x = 0
        self.y = 0

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.enemy = None
        self.item = None

