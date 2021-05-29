import time
import copy
import random
import os
from sys import platform

generations = 1000
timer = .01
evolute = .00


ymax = 50
xmax = 40

game = []

saveorigin = []
savestates = []



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
rand = []
pulseline = [[20, 6], [20, 7], [20, 8], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [20, 15]]
pulselarg = [[14, 3], [20, 3], [14, 4], [20, 4], [14, 5], [15, 5], [19, 5], [20, 5], [10, 7], [11, 7], [12, 7], [15, 7], [16, 7], [18, 7], [19, 7], [22, 7], [23, 7], [24, 7], [12, 8], [14, 8], [16, 8], [18, 8], [20, 8], [22, 8], [14, 9], [15, 9], [19, 9], [20, 9], [14, 11], [15, 11], [19, 11], [20, 11], [12, 12], [14, 12], [16, 12], [18, 12], [20, 12], [22, 12], [10, 13], [11, 13], [12, 13], [15, 13], [16, 13], [18, 13], [19, 13], [22, 13], [23, 13], [24, 13], [14, 15], [15, 15], [19, 15], [20, 15], [14, 16], [20, 16], [14, 17], [20, 17]]
glidergun = [[25, 1], [23, 2], [25, 2], [13, 3], [14, 3], [21, 3], [22, 3], [35, 3], [36, 3], [12, 4], [16, 4], [21, 4], [22, 4], [35, 4], [36, 4], [1, 5], [2, 5], [11, 5], [17, 5], [21, 5], [22, 5], [1, 6], [2, 6], [11, 6], [15, 6], [17, 6], [18, 6], [23, 6], [25, 6], [11, 7], [17, 7], [25, 7], [12, 8], [16, 8], [13, 9], [14, 9]]
#End Presets


preset = pulseline

if preset == "rand":
    points = random.randint(0, ymax*xmax)
    for point in range(points):
        rand.append([])
    for point in range(len(rand)):
        rand[point] = [random.randint(0, xmax-1), random.randint(0, ymax-1)]
    for pos in rand:
        game[pos[1]][pos[0]] = 1
else:
    for pos in preset:
        game[pos[1]][pos[0]] = 1



game = """[
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
    
    savestates.append(newgame)

    return newgame

def arreplace(gamearray, target, replaced, target2, replaced2):
    arr = copy.deepcopy(gamearray)
    for x in range(len(arr)):
        if arr[x] == target:
            arr[x] = replaced
        if arr[x] == target2:
            arr[x] = replaced2
    
    return arr


saveorigin = copy.deepcopy(game)

print(f"______________gen: original_______")
for y in game:
    print(arreplace(y, 0, ' ', 1, "▘"))

class releaseMe(Exception):
    pass

try:
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
        
        for save in savestates[:-1]:
            if save == newgame:
                print(f"Provably stable or empty after {gen+2} generations.")
                for y in saveorigin:
                    print(arreplace(y, 0, ' ', 1, "▘"))
                raise releaseMe
except releaseMe:
    pass

def export():
    exported = []
    for y in ren(saveorigin):
        for x in ren(saveorigin[y]):
            if saveorigin[y][x] == 1:
                exported.append([x,y])
    
    return exported

print(export())
        