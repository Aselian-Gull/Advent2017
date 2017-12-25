print ("This cannot continue.  Advent of Code 2017, Day 23.")

import math

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_23.txt", "r")
inputLines = f.readlines()
f.close()


registers = {}
sounds = []
prints = 0
stacktrace = []
mulCount = 0

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
    elif tokens[0] == "sub":
        cur = regs.get(tokens[1], 0)
        cur = cur - getRegVal(regs, tokens[2])
        regs[tokens[1]] = cur
    elif tokens[0] == "mul":
        cur = regs.get(tokens[1], 0)
        cur = cur * getRegVal(regs, tokens[2])
        regs[tokens[1]] = cur
        
while (curRow < len(inputLines) and curRow >= 0):
    tokens = inputLines[curRow].strip('\n').split(' ')
    if tokens[0] == "jnz":
        if getRegVal(registers, tokens[1]) != 0:
            curRow = curRow + getRegVal(registers, tokens[2])
            continue
    else:
        if(tokens[0] == "mul"):
            mulCount = mulCount + 1
        updateRegs(registers, tokens)
    curRow = curRow + 1
    
print("\n%d multiply operations run." % mulCount)

print("\nAfter some careful analysis, I've determined that this program is computing whether something is prime.")
print("By brute force.")
print("So let's just write something to do that a little more efficiently.")
# Parse the initial values out.
curRow = 0
registers["a"] = 1
while (curRow < 8 and curRow >= 0): # just run enough to get the keys.
    tokens = inputLines[curRow].strip('\n').split(' ')
    if tokens[0] == "jnz":
        if getRegVal(registers, tokens[1]) != 0:
            curRow = curRow + getRegVal(registers, tokens[2])
            continue
    else:
        if(tokens[0] == "mul"):
            mulCount = mulCount + 1
        updateRegs(registers, tokens)
    curRow = curRow + 1

b = getRegVal(registers, "b")
c = getRegVal(registers, "c")
inc = int(inputLines[len(inputLines)-2].strip('\n').split(' ')[2]) * -1
print("\nProgram analyzed.  We check values from %d to %d (inclusive) with an increment of %d." % (b, c, inc))

unprimes = 0
while b <= c:
    for fact in range(2, int(math.sqrt(b))):
        if b % fact == 0:
            unprimes = unprimes + 1
            break
    b = b + inc
        
print("\nProcessing complete.  %d of the numbers checked were non-prime." % unprimes)