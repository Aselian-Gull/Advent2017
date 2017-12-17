print ("It's the most wonderful challenge of the year!  Advent of Code 2017, Day 15.")

# This one takes a while.
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_15.txt", "r")
inputLines = f.readlines()
f.close()

genStarts = []
for line in inputLines:
    tokens = line.rstrip().split(' ')
    genStarts.append(int(tokens[4]))
genFacts = [16807, 48271]
magic = 2147483647
mask = 0xFFFF

def nextA(curA):
    return (curA * genFacts[0]) % magic

def nextB(curB):
    return (curB * genFacts[1]) % magic

def low16(curA, curB):
    if((curA & mask) == (curB & mask)):
        return 1
    else:
        return 0

# GENERATOR DUEL
a, b = genStarts[0], genStarts[1]
matches = 0

for pairCount in range(40000000):
    matches = matches + low16(a, b)
    a, b = nextA(a), nextB(b)

print("The first judging matched %d pairs" % matches)

# OKAY NOW RAMP IT UP

def nextPickyA(curA):
    temp = nextA(curA)
    while (temp % 4) != 0:
        temp = nextA(temp)
    return temp

def nextPickyB(curB):
    temp = nextB(curB)
    while (temp % 8) != 0:
        temp = nextB(temp)
    return temp

a, b = genStarts[0], genStarts[1]
hardMatch = 0
for pairCount in range(5000000):
    hardMatch = hardMatch + low16(a, b)
    a, b = nextPickyA(a), nextPickyB(b)
    
print ("The second judging found %d matching pairs.\n" % hardMatch)
print ("There'll be lots of code stories")
print ("And tales of the glories")
print ("Of advent challenges done long ago!")