print ("Dawn of the final stretch.  Advent of Code 2017, Day 21.")

import time

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_21.txt", "r")
inputLines = f.readlines()
f.close()

initGrid = [".#.", "..#", "###"]

def rotateGrid(grid):
    newGrid = []
    for col in range(len(grid)):
        tempRow = ""
        for row in range(len(grid)):
            tempRow = tempRow + grid[len(grid) - 1 - row][col] 
        newGrid.append(tempRow)
    return newGrid

def flipGrid(grid):
    newGrid = []
    for row in range(len(grid)):
        newGrid.append(grid[row][::-1])
    return newGrid

def twistGrid(grid, flip, rot):
    newGrid = grid.copy()
    if(flip > 0):
        newGrid = flipGrid(newGrid)
    for _ in range(0, rot):
        newGrid = rotateGrid(newGrid)
    return newGrid

def lightCount(grid):
    return sum(sum(1 for col in row if col == '#') for row in grid)

def modifyGrid(grid):
    newGrid = []
    # Okay.  Split into components.
    size = len(grid)
    numLit = lightCount(grid)
    if size > 2 and size % 2 == 0:
        for row in range(0, size, 2):
            newGrid.append("")
            newGrid.append("")
            newGrid.append("")
            for col in range(0, size, 2):
                tempGrid = [grid[row][col:col+2], grid[row+1][col:col+2]]
                tempGrid = modifyGrid(tempGrid)
                for d in range(3):
                    newGrid[int(row*3/2) + d] = newGrid[int(row*3/2) + d] + tempGrid[d]
        return newGrid
    elif size > 3 and size % 3 == 0:
        for row in range(0, size, 3):
            newGrid.append("")
            newGrid.append("")
            newGrid.append("")
            newGrid.append("")
            for col in range(0, size, 3):
                tempGrid = [grid[row][col:col+3], grid[row+1][col:col+3], grid[row+2][col:col+3]]
                tempGrid = modifyGrid(tempGrid)
                for d in range(4):
                    newGrid[int(row*4/3) + d] = newGrid[int(row*4/3) + d] + tempGrid[d]
        return newGrid
    else:
        # Try every state, every rule.
        for line in inputLines:
            io = line.strip('\n').split(' ')
            inputRule = io[0].split('/')
            if len(inputRule) != size:
                continue    # Unmatchable.
            if(lightCount(inputRule) != numLit):
                continue    # Unmatchable.    
            for flip in range(2):
                for rot in range(4):
                    tempGrid = twistGrid(grid, flip, rot)
                    found = sum(1 for row in range(size) if inputRule[row] == tempGrid[row])
                    if found == size:
                        tempGrid = io[2].split('/')
                        return tempGrid
                        
    print("NO RULE FOUND THIS IS BROKEEEEEN")
    return[]

# Okay.  Now let's do the thing.
startTime = time.process_time()
loopTime = startTime
def updateLoopTime(curTime, counter):
    tempTime = time.process_time()
    print("Loop %d ran in %f s" % (counter, tempTime-curTime))
    return tempTime

grid5 = initGrid.copy()
for timeRun in range(0,5):
    grid5 = modifyGrid(grid5)
    loopTime = updateLoopTime(loopTime, timeRun)

print("%d lit after five iterations." % lightCount(grid5))

grid18 = grid5.copy()
for timeRun in range(5, 18):
    grid18 = modifyGrid(grid18)
    loopTime = updateLoopTime(loopTime, timeRun)

lights = 0
for row in grid18:
    lights = lights + sum(1 for col in row if col == '#')
print("%d lit after eighteen iterations." % lightCount(grid18))

print("Total elapsed time: %f" % (loopTime - startTime))