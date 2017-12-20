print ("I can hear cheerful babbling...It's assembly time.  Advent of Code 2017, Day 18.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_18.txt", "r")
inputLines = f.readlines()
f.close()

registers = {}
sounds = []
prints = 0
stacktrace = []

curRow = 0
def getRegVal(regs, key):
    temp = 0
    try:
        temp = int(key)
    except ValueError:
        temp = regs.get(key, 0)
    return temp

def updateRegs(regs, tokens):
    if tokens[0] == "set":
        regs[tokens[1]] = getRegVal(regs, tokens[2])
    elif tokens[0] == "add":
        cur = regs.get(tokens[1], 0)
        cur = cur + getRegVal(regs, tokens[2])
        regs[tokens[1]] = cur
    elif tokens[0] == "mul":
        cur = regs.get(tokens[1], 0)
        cur = cur * getRegVal(regs, tokens[2])
        regs[tokens[1]] = cur
    elif tokens[0] == "mod":
        cur = regs.get(tokens[1], 0)
        cur = cur % getRegVal(regs, tokens[2])
        regs[tokens[1]] = cur

while (curRow < len(inputLines) and curRow >= 0):
    tokens = inputLines[curRow].strip('\n').split(' ')
    if tokens[0] == "snd":
        sounds.append(getRegVal(registers, tokens[1]))
        # Echos register.
    elif tokens[0] == "rcv":
        if getRegVal(registers, tokens[1]) != 0:
            print("rcv run; last snd was %d" % sounds.pop())
            break
    elif tokens[0] == "jgz":
        if getRegVal(registers, tokens[1]) > 0:
            curRow = curRow + getRegVal(registers, tokens[2])
            continue
    else:
        updateRegs(registers, tokens)
    curRow = curRow + 1
    
regA = {}
regB = {}
AtoB = []
BtoA = []

regA["p"] = 0
regB["p"] = 1

# Okay, parallel.  ...okay.
curA = 0
curB = 0
aSent = 0
BSent = 0
steps = 0

while (curA < len(inputLines) and curA >= 0 and curB < len(inputLines) and curB >= 0):
    alock = 0
    block = 0
    tokens = inputLines[curA].strip('\n').split(' ')
    if tokens[0] == "snd":
        AtoB.append(getRegVal(regA, tokens[1]))
        aSent = aSent + 1
        # Echos register.
    elif tokens[0] == "rcv":
        if len(BtoA) == 0:
            alock = 1
        else:
            regA[tokens[1]] = BtoA.pop(0)
    elif tokens[0] == "jgz":
        if getRegVal(regA, tokens[1]) > 0:
            curA = curA + getRegVal(regA, tokens[2])
            continue
    else:
        updateRegs(regA, tokens)
    if alock == 0:
        curA = curA + 1
    
    tokens = inputLines[curB].strip('\n').split(' ')
    if tokens[0] == "snd":
        BtoA.append(getRegVal(regB, tokens[1]))
        BSent = BSent + 1
        # Echos register.
    elif tokens[0] == "rcv":
        if len(AtoB) == 0:
            block = 1
        else:
            regB[tokens[1]] = AtoB.pop(0)
    elif tokens[0] == "jgz":
        if getRegVal(regB, tokens[1]) > 0:
            curB = curB + getRegVal(regB, tokens[2])
            continue
    else:
        updateRegs(regB, tokens)
    
    if block == 0:
        curB = curB + 1
    if alock > 0 and block > 0:
        print("Alert.  Threads are deadlocked.")
        break
        
print("Program 0 terminated at line %d after sending %d messages." % (curA, aSent))
print("Program 1 terminated at line %d after sending %d messages." % (curB, BSent))