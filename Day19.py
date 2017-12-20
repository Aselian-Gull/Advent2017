print ("All we need to do is solve seven challenges at once.  Advent of Code 2017, Day 19.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_19.txt", "r")
inputLines = f.readlines()
f.close()

print ("It's been a good run.")

curX = 0
curY = 0
curDir = 0 # 0 down, 1 left, 2 right, 3 up
accLet = ""

def getLeft(x, y):
    if x > 0:
        return inputLines[y][x-1]
    else:
        return ' '
def getRight(x, y):
    if x + 1 < len(inputLines[y]):
        return inputLines[y][x+1]
    else:
        return ' '
def getUp(x, y):
    if y > 0:
        return inputLines[y-1][x]
    else:
        return ' '
def getDown(x, y):
    if y + 1 < len(inputLines):
        return inputLines[y+1][x]
    else:
        return ' '
    
def getPrev(x, y, dir):
    if dir == 0:
        return getUp(x, y)
    if dir == 1:
        return getRight(x, y)
    if dir == 2:
        return getLeft(x, y)
    if dir == 3:
        return getDown(x, y)

def getNext(x, y, dir):
    return getPrev(x, y, (3-dir))

def isEnd(x, y):
    dirs = []
    dirs.append(getLeft(x,y))
    dirs.append(getDown(x,y))
    dirs.append(getUp(x,y))
    dirs.append(getRight(x,y))
    return sum(1 for c in dirs if c != ' ' and c != '\n')

# FIND THE start
for x in range(len(inputLines[0])):
    if inputLines[0][x] != ' ':
        curX = x
        break

print ("Start at %d %d" % (curX, curY))
# traverse
steps = 1 # initial step

while len(accLet) == 0 or isEnd(curX, curY) > 1:
    if curDir == 0: # Down
        curY = curY + 1
    if curDir == 1: # Left
        curX = curX - 1
    if curDir == 2: # Right
        curX = curX + 1
    if curDir == 3: # Up
        curY = curY - 1
    curChar = inputLines[curY][curX]
    if(curChar >= 'A' and curChar <= 'Z'):
        accLet = accLet + curChar
        print(accLet)
    if(curChar == '+'): # turn
        for dTemp in range(0, 4):
            if dTemp == (3 - curDir):
                continue
            if getNext(curX, curY, dTemp) != ' ':
                curDir = dTemp
                break
    steps = steps + 1

print ("%d steps to find %s" % (steps, accLet))