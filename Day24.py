print ("Glory to mankind.  Advent of Code 2017, Day 24.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_24.txt", "r")
inputLines = f.readlines()
f.close()

print("It's dominoes.  Let's hit this problem with a sledgehammer.")

pieces = []
for line in inputLines:
    tokens = line.strip('\n').split('/')
    pieces.append([int(tokens[0]), int(tokens[1])])

def bestBridge(curBridge, curId, rule):
    bestStr = 0
    bestLen = 0
    for idx in range(0, len(pieces)):
        if curBridge.count(idx) != 0:
            continue
        for e in [0, 1]: # check both ends
            if pieces[idx][e] == curId:
                tempBridge = curBridge.copy()
                tempBridge.append(idx)
                tempStr, tempLen = bestBridge(tempBridge, pieces[idx][1-e], rule)
                tempStr = tempStr + pieces[idx][0] + pieces[idx][1]
                tempLen = tempLen + 1
                if ((rule == 0 or tempLen == bestLen) and tempStr > bestStr) or (rule == 1 and tempLen > bestLen):
                    bestStr = tempStr
                    bestLen = tempLen
                break # don't check both ends once we match one
    return bestStr, bestLen

print ("Best bridge using strength alone has strength %d, length %d" % bestBridge([], 0, 0))
print ("Longest strongest bridge has strength %d, length %d" % bestBridge([], 0, 1))
print ("There's a more efficient solution.  Someday I might even write it.")
    