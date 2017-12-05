import math
import itertools
#import solveadventquickly....nah, let's at least put a tiny bit of effort in.

print("Good evening.  Advent of Code 2017, Day 2.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_2.txt", "r")
inputfile = f.readlines()
f.close()

# Need two totals.
totalsum = 0
totalquot = 0

# Simple iteration.  Checksums aren't bad.
for line in inputfile:
    minval = 999999             # Assumes values less than a million.  Should find Python's maxint.
    maxval = 0
    vallist = []                # This was easier for handling the 'find quotient' part.
    for token in line.split("\t"):
        if token == "\n":
            continue            # Yeaaaah, split still got endl included.
        vallist.append(int(token))
    # Easy part: max minus min.  We can even just run helpers on the list.
    totalsum = totalsum + (max(vallist) - min(vallist))
    
    # Okay, now find the best quotient.  Let's brute-force it.
    for x,y in itertools.product(range(0, len(vallist)), range(0, len(vallist))):
        if(x == y):
            continue
        testval = vallist[x] / vallist[y]
        if(math.floor(testval) == testval):
            totalquot = totalquot + testval
            break   # Minor risk: We assume nearly everything is coprime.
    
# End of nested loop.  My one gripe about python is that it's harder to see where scope ends.
    
print ("Total checksum: %d" % totalsum)
print ("Total quotients: %d" % totalquot)
