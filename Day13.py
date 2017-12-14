print("This just went badly.  Advent of Code 2017, Day 13.")
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_13.txt", "r")
inputLines = f.readlines()
f.close()

depths = {}
numScans = 0
for line in inputLines:
    tokens = line.strip('\n').split(':')
    depths[int(tokens[0])] = int(tokens[1])
    numScans = max(numScans, int(tokens[0]))

# Right.  Calculate the severity for starting immediately.
severity = 0
for col in depths:
    depth = depths[col]
    cycle = 2 * (depth - 1)
    if depth != 0 and col % cycle == 0:
        severity = severity + (depth * col)
        
print ("Severity is equal to %d" % severity)

# Now just brute-force it.  Can we do better?
for tryDelay in range(0, 10000000):
    canPass = 1
    for idx in depths:
        depth = depths[idx]
        cycle = 2 * (depth - 1)
        if ((tryDelay + idx) % cycle) == 0:
            canPass = 0
            break
    if canPass > 0:
        print("If we wait %d picoseconds, we'll make it through." % tryDelay)
        break
    
# The following are legacy functions from a failed attempt.

def moveScanners(posVec, dirVec):
    for idx in range(0, numScans + 1):
        depth = depths.get(idx, 0)
        if depth == 0:
            continue
        posVec[idx] = posVec[idx] + dirVec[idx]
        if posVec[idx] + 1 == depth:
            dirVec[idx] = -1
        elif posVec[idx] == 0:
            dirVec[idx] = 1


def delaySeverity(delayTest):
    scannerPos = []
    scannerDir = []
    
    for idx in range(0, numScans+1):
        scannerPos.append(0)
        scannerDir.append(1)
                
    for t in range(0, delayTest):
        moveScanners(scannerPos, scannerDir)        
    totalSeverity = 0
    curPos = 0
    while curPos < numScans:
        moveScanners(scannerPos, scannerDir)
        curPos = curPos + 1
        depth = depths.get(curPos, 0)
        if scannerPos[curPos] == 0 and depth != 0:
            totalSeverity = totalSeverity + (curPos * depths.get(curPos, 0))
    return totalSeverity
