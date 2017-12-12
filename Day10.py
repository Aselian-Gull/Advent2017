print("Good evening.  Advent of Code 2017, Day 10.")

maxlen = 256
def day10Hash(values, keys, skipPos):    
    for key in keys:
        temprange = []
        for tempIdx in range(skipPos[0], skipPos[0] + key):
            temprange.append(values[tempIdx % maxlen])
        temprange.reverse()
        for tempIdx in range(0, + key):
            values[(skipPos[0] + tempIdx) % maxlen] = temprange[tempIdx]
        skipPos[0] = (skipPos[0] + key + skipPos[1]) % maxlen
        skipPos[1] = skipPos[1] + 1
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_10.txt", "r")
inStream = f.read()
f.close()

keyInts = []
for token in inStream.strip('\n').split(','):
    keyInts.append(int(token))

intvalues = []
sparseVals = []
for item in range(0, maxlen):
    intvalues.append(item)
    sparseVals.append(item)
    
intSkipPos = [0, 0]
day10Hash(intvalues, keyInts, intSkipPos)
print ("The product of the first two hashed ints is %d" % (intvalues[0] * intvalues[1]))

# Right.  Now let's really ramp things up.
keyChrs = []
for token in inStream.strip('\n'):
    keyChrs.append(ord(token))
keyChrs.append(17)
keyChrs.append(31)
keyChrs.append(73)
keyChrs.append(47)
keyChrs.append(23)

charSkipPos = [0, 0]
for timeRun in range(0, 64):
    day10Hash(sparseVals, keyChrs, charSkipPos)

# Now XOR it all.
dense2 = 0
for charIdx in range(0, maxlen):
    if(charIdx % 16 == 0):
        dense2 = dense2 << 8
    dense2 = dense2 ^ sparseVals[charIdx]
print(hex(dense2))