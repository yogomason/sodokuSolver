moves = 0
ans = None
import time
from copy import deepcopy
# grid = [
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-','-','-','-','-'],
# ]
grid = [
    [5,3,'-','-',7,'-','-','-','-'],
    [6,'-','-',1,9,5,'-','-','-'],
    ['-',9,8,'-','-','-','-',6,'-'],
    [8,'-','-','-',6,'-','-','-',3],
    [4,'-','-',8,'-',3,'-','-',1],
    [7,'-','-','-',2,'-','-','-',6],
    ['-',6,'-','-','-','-',2,8,'-'],
    ['-','-','-',4,1,9,'-','-',5],
    ['-','-','-','-',8,'-','-',7,9],
]

# grid = [
#     ['-','-','-','-','-','-','-','-','-'],
#     ['-','-','-','-','-',3,'-',8,5],
#     ['-','-',1,'-',2,'-','-','-','-'],
#     ['-','-','-',5,'-',7,'-','-','-'],
#     ['-','-',4,'-','-',1,'-','-','-'],
#     ['-',9,'-','-','-','-','-','-','-'],
#     [5,'-','-','-','-','-','-',7,3],
#     ['-','-',2,'-',1,'-','-','-','-'],
#     ['-','-','-','-',4,'-','-','-',9],
# ]



def findstartcoords(grid):
    for x in range(0,8):
        for y in range(0,8):
            if grid[x][y] == '-':
                return x, y

def makedict():
    mydict = {}
    for x in range(1,10):
        mydict[x] = 0
    return mydict

def verifyrow(grid, row):
    mydict = makedict()
    for num in grid[row]:
        if num == '-':
            pass
        elif mydict[num] == 1:
            return False
        else:
            mydict[num] += 1
    return True

def verifycolumn(grid, column):
    mydict = makedict()
    for i in range(0,9):
        num = grid[i][column]
        if num == '-':
            pass
        elif mydict[num] == 1:
            return False
        else:
            mydict[num] += 1
    return True

def verifysquare(grid, x, y):
    mydict = makedict()
    newx, newy = squarerow(x/3), squarerow(y/3)
    for i in range(0,3):
        for ii in range(0,3):
            num = grid[newx+i][newy+ii]
            if num == '-':
                pass
            elif mydict[num] == 1:
                return False
            else:
                mydict[num] += 1
    return True

def squarerow(x):
    if x < 1:
        return 0
    elif x < 2:
        return 3
    elif x < 3:
        return 6

def solve(grid, x=0, y=0):
    global moves, start, ans
    if y == 8 and grid[x][y] != '-':
        if x == 8:
            ans = deepcopy(grid)
            print(moves)
            print(time.time() - start)
            return "b"
        c = solve(grid, x+1, 0)
        if c == "b":
            return "b"
        return
    elif grid[x][y] != '-':
        c = solve(grid, x, y+1)
        if c == "b":
            return "b"
        else:
            return
    while True:
        if grid[x][y] == '-':
            grid[x][y] = 1

        while not verifysquare(grid, x, y) or not verifyrow(grid, x) or not verifycolumn(grid, y):
            grid[x][y] += 1
            moves += 1
            if grid[x][y] == 10:
                grid[x][y] = '-'
                return
        if verifysquare(grid, x, y) and verifyrow(grid, x) and verifycolumn(grid, y):
            if y == 8 and x == 8:
                ans = deepcopy(grid)
                print(moves)
                print(time.time() - start)
                return "b"
            if y == 8:
                c = solve(grid, x+1, 0)
                if c == "b":
                    return "b"
                grid[x][y] += 1
                moves += 1
                if grid[x][y] == 10:
                    grid[x][y] = '-'
                    return
            else:
                c = solve(grid, x, y+1)
                if c == "b":
                    return "b"
                grid[x][y] += 1
                moves += 1
                if grid[x][y] == 10:
                    grid[x][y] = '-'
                    return
start = time.time()
x, y = findstartcoords(grid)
solve(grid, x, y)
print(ans)