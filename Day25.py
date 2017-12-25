print ("Merry Christmas!.  Advent of Code 2017, Day 25.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_25.txt", "r")
inputLines = f.readlines()
f.close()

numStepsToCheck = int(inputLines[1].split(' ')[5])

myTuringTape = {}

zeroWrites = {}
zeroIncs = {}
zeroNexts = {}
oneNexts = {}
oneWrites = {}
oneIncs = {}

initState = inputLines[0].strip('\n').split(' ')[3].strip('.')

for L in range(3,len(inputLines), 10):
    rule = inputLines[L].strip('\n').split(' ')[2].strip(':')
    zeroWrites[rule] = int(inputLines[L+2].strip('\n').split(' ')[-1].strip('.'))
    if inputLines[L+3].strip('\n').split(' ')[-1] == "left.":
        zeroIncs[rule] = -1
    else:
        zeroIncs[rule] = 1
    zeroNexts[rule] = inputLines[L+4].strip('\n').split(' ')[-1].strip('.')
    
    oneWrites[rule] = int(inputLines[L+6].strip('\n').split(' ')[-1].strip('.'))
    if inputLines[L+7].strip('\n').split(' ')[-1] == "left.":
        oneIncs[rule] = -1
    else:
        oneIncs[rule] = 1
    oneNexts[rule] = inputLines[L+8].strip('\n').split(' ')[-1].strip('.')
    
print ("Rules have been parsed.")

print("Starting Turing machine at position %s." % initState)

curPos = 0
curState = initState
for step in range(numStepsToCheck):
    if myTuringTape.get(curPos, 0) == 0:
        myTuringTape[curPos] = zeroWrites[curState]
        curPos = curPos + zeroIncs[curState]
        curState = zeroNexts[curState]
    else:
        myTuringTape[curPos] = oneWrites[curState]
        curPos = curPos + oneIncs[curState]
        curState = oneNexts[curState]

checkSum = sum(v for k, v in myTuringTape.items())
print("Pausing after %d steps at state %s, position %d; checksum is %d."
      % (numStepsToCheck, curState, curPos, checkSum))

print("\nCongratulations!  Everything has been done in Python!")