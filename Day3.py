#import math
import itertools
#import solveadventquickly....nah, let's at least put a tiny bit of effort in.

print("Good evening.  Advent of Code 2017, Day 3.")

# No file today, this is the whole input.
keyvalue = 361527

# Part 1: Walk along the spiral.
dval = 0
dmax = 1
ddir = 0
x = 0
y = 0

for i in range(1, keyvalue):
    if(ddir == 0):
        x = x + 1
    elif(ddir == 1):
        y = y + 1
    elif(ddir == 2):
        x = x - 1
    elif(ddir == 3):
        y = y - 1
        
    dval = dval + 1
    if(dval >= dmax):
        dval = 0
        ddir = (ddir + 1) % 4
        if(ddir % 2 == 0):
            dmax = dmax + 1

distval = abs(x) + abs(y)
print("%d is located at %d, %d with a distance of %d" % (keyvalue, x, y, distval))

# Build a 101x101 grid and hope that's enough to accumulate the answer.
grid = []
for row in range(0, 101):
    grid.append([])
    for col in range(0, 101):
        grid[row].append(0)

x = 50
y = 50
dval = 0
dmax = 1
ddir = 0

grid[x][y] = 1
for i in range(0, 10000):
    # Sum the surroundings.
    for delx, dely in itertools.product(range(-1, 2), range(-1, 2)):
        if(delx == 0 and dely == 0):
            continue
        grid[x][y] = grid[x][y] + grid[x+delx][y+dely]
    if(grid[x][y] > keyvalue):
        print("Value at %d %d is %d" % (x, y, grid[x][y]))
        break
    # Walk along the spiral.
    if(ddir == 0):
        x = x + 1
    elif(ddir == 1):
        y = y + 1
    elif(ddir == 2):
        x = x - 1
    elif(ddir == 3):
        y = y - 1
        
    dval = dval + 1
    if(dval >= dmax):
        dval = 0
        ddir = (ddir + 1) % 4
        if(ddir % 2 == 0):
            dmax = dmax + 1

print("That's the end.")