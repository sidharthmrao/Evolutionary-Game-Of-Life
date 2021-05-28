import time
import copy

game = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
]

newgame = [
]

def reset():
    newgame = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    return newgame

def ren(arr):
    return range(len(arr))

def surround(y, x):
    possible = [[y-1,x], [y+1,x], [y,x-1], [y,x+1]]

    total = [False, False, False, False]

    for position in ren(possible):
        run = True
        for coordinate in possible[position]:
            if coordinate >= 14 or coordinate == -1:
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
            if check<=1:
                newgame[y][x] = 0
            if check>1:
                newgame[y][x] = 1
            if check == 4:
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

generations = 5
timer = 1
evolute = 0

print(f"______________gen: original_______")
for y in game:
    print(arreplace(y, 0, ' ', 1, '1'))

for gen in range(generations):
    time.sleep(timer)
    newgame = reset()
    game = update()
    print(f"______________gen: {gen+2}____________")
    for y in newgame:
        print(arreplace(y, 0, ' ', 1, '1'))
    