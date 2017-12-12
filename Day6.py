#import solveadventquickly....oh wait, I have to finish writing it.

print("Good evening.  Advent of Code 2017, Day 6.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_6.txt", "r")
inputfile = f.read()
f.close()

inputwords = inputfile.strip('\n').split('\t')
inputvals = []
for word in inputwords:
    inputvals.append(int(word))

def redistribute (state):
    maxIdx = 0
    numBins = len(state)
    for idx in range(0, numBins):
        if state[idx] > state[maxIdx]:
            maxIdx = idx
    # Okay.  We have our highest value.  Now push.
    newState = state[:]
    blocks = newState[maxIdx]
    newState[maxIdx] = 0
    idx = (maxIdx + 1) % numBins
    while blocks > 0:
        newState[idx] = newState[idx] + 1
        blocks = blocks - 1
        idx = (idx + 1) % numBins
    return newState
        
total = 0
loopstart = 0
statesSeen = []
currentState = inputvals
statesSeen.append(currentState[:])

testState = redistribute(currentState)

while 1:
    currentState = redistribute(currentState)
    total = total + 1
    exists = 0
    for stateIdx in range(0,len(statesSeen)):
        if statesSeen[stateIdx] == currentState:
            exists = 1
            loopstart = stateIdx
            break
    if exists != 0:
        break
    else:
        statesSeen.append(currentState[:])

print("We approach infinity on run %d" % total)
print("The infinite loop is length %d" % (total - loopstart))

# Now let's animate it for kicks.

