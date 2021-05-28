import time
import copy
import random
import os
from sys import platform

generations = 1000
timer = .01
evolute = .00


ymax = 40
xmax = 40

game = []

def generate_board(ymax, xmax):
    board = []
    for y in range(ymax):
        board.append([])
    for x in range(xmax):
        for y in board:
            y.append(0)
    return board

game = generate_board(ymax, xmax)

#Presets
none = []
pulsar = [[10,7],[10,13],[11,7],[11,13],[12,7],[12,8],[12,12],[12,13],[14,3],[14,4],[14,5],[14,8],[14,9],[14,11],[14,12],[14,15],[14,16],[14,17],[15,5],[15,7],[15,9],[15,11],[15,13],[15,15],[16,7],[16,8],[16,12],[16,13],[18,7],[18,8],[18,12],[18,13],[19,5],[19,7],[19,9],[19,11],[19,13],[19,15],[20,3],[20,4],[20,5],[20,8],[20,9],[20,11],[20,12],[20,15],[20,16],[20,17],[22,7],[22,8],[22,12],[22,13],[23,7],[23,13],[24,7],[24,13]]
glider = [[1, 5],[1, 6],[2, 5],[2, 6],[11, 5],[11, 6],[11, 7],[12, 4],[12, 8],[13, 3],[13, 9],[14, 3],[14, 9],[15, 6],[16, 4],[16, 8],[17, 5],[17, 6],[17, 7],[18, 6],[21, 3],[21, 4],[21, 5],[22, 3],[22, 4],[22, 5],[23, 2],[23, 6],[25, 1],[25, 2],[25, 6],[25, 7],[35, 3],[35, 4],[36, 3],[36, 4]]
#End Presets


preset = glider

for pos in preset:
    game[pos[1]][pos[0]] = 1

"""game = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
]"""

newgame = [
]

def reset():
    newgame = generate_board(ymax, xmax)

    return newgame

def ren(arr):
    return range(len(arr))

def surround(y, x):
    possible = [[y-1,x], [y+1,x], [y,x-1], [y,x+1], [y-1, x-1], [y+1, x-1], [y-1, x+1], [y+1, x+1]]

    total = [False, False, False, False, False, False, False, False,]

    for position in ren(possible):
        run = True
        for coordinate in range(len(possible[position])):
            if coordinate == 0:
                if possible[position][coordinate] >= ymax or possible[position][coordinate] == -1:
                    run = False
            if coordinate == 1:
                if possible[position][coordinate] >= xmax or possible[position][coordinate] == -1:
                    run = False
            
        if run:
            if game[possible[position][0]][possible[position][1]] == 1:
                total[position] = True

    count = 0
    for check in total:
        if check:
            count+=1

    return count

def update():
    for y in range(len(game)):
        for x in range(len(game[y])):
            check = surround(y,x)

            if check == 2:
                newgame[y][x] = copy.deepcopy(game[y][x])
            elif check == 3:
                newgame[y][x] = 1
            else:
                newgame[y][x] = 0
                
            evolve = random.random()
            if evolve <= evolute:
                newgame[y][x] = 1
            if evolve >= 1-evolute:
                newgame[y][x] = 0
    return newgame

def arreplace(gamearray, target, replaced, target2, replaced2):
    arr = copy.deepcopy(gamearray)
    for x in range(len(arr)):
        if arr[x] == target:
            arr[x] = replaced
        if arr[x] == target2:
            arr[x] = replaced2
    
    return arr




print(f"______________gen: original_______")
for y in game:
    print(arreplace(y, 0, ' ', 1, "▘"))

for gen in range(generations):
    time.sleep(timer)
    newgame = reset()
    game = update()
    if platform == 'linux' or platform == 'linux2':
        os.system('clear')
    else:
        os.system('cls')
    print(f"______________gen: {gen+2}____________")
    for y in newgame:
        print(arreplace(y, 0, ' ', 1, "▘"))
    