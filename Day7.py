#import solveadventquickly....oh wait, I have to finish writing it.

print("Good evening.  Advent of Code 2017, Day 7.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_7.txt", "r")
inputfile = f.readlines()
f.close()

names = []
nameLookup = {}
values = []
supportNames = []
isRoot = []

for line in inputfile:
    line = line.strip('\n')
    tokens = line.split(" ")
    nameLookup[tokens[0]] = len(names)
    names.append(tokens[0])
    values.append(int(tokens[1].strip('()')))
    supports = []
    if len(tokens) > 3:
        for support in tokens[3:]:
            supports.append(support.strip('\n').strip(','))
    supportNames.append(supports)
    isRoot.append(1)

towerVals = values[:]

for idx in range(0, len(inputfile)):
    for child in supportNames[idx]:
        isRoot[nameLookup[child]] = 0

baseIdx = 0
for idx in range(0, len(inputfile)):
    if isRoot[idx] > 0:
        print ("We have a program carrying the weight of the world: %s" % names[idx])
        baseIdx = idx
        break

def sumTower(idx):
    for supports in supportNames[idx]:
        sumTower(nameLookup[supports])
        towerVals[idx] = towerVals[idx] + towerVals[nameLookup[supports]]
        
sumTower(baseIdx)
# Now find the worst path.


idx = baseIdx
delta = 0
while len(supportNames[idx]) > 0:
    tempIdx = idx
    children = []
    for support in supportNames[idx]:
        children.append(nameLookup[support])
    if len(children) > 2:
        if(towerVals[children[0]] != towerVals[children[1]]):
            base = towerVals[children[2]]
            if(towerVals[children[0]] != base):
                tempIdx = children[0]
                delta = base - towerVals[tempIdx]
            else: # towerVals[children[1]] is the aberration.
                tempIdx = children[1]
                delta = base - towerVals[tempIdx]
        else:
            base = towerVals[children[0]]
            for childIdx in children:
                if towerVals[childIdx] != base:
                    tempIdx = childIdx
                    delta = base - towerVals[childIdx]
    if tempIdx != idx:
        idx = tempIdx
    else:
        break

print ("%s was the source of imbalance, and the value of %d must become %d" % (names[idx], values[idx], values[idx] + delta))