#import math
#import hashlib

print("Good evening.  Advent of Code 2017, Day 1.")

f = open("/home/smacgil/Development/Advent/input2017_1.txt", "r")
inputfile = f.read()
f.close()

totalone = 0
totalhalf = 0
maxval = len(inputfile) - 1 # EOL is a thing.
halfval = int(maxval / 2)   # Convenience.

for digit in range(0, maxval):
    nextone = (digit + 1) % maxval
    nexthalf = (digit + halfval) % maxval
    # Compare chars, and convert if adding.
    if(inputfile[digit] == inputfile[nextone]):
        totalone = totalone + int(inputfile[digit])
    if(inputfile[digit] == inputfile[nexthalf]):
        totalhalf = totalhalf + int(inputfile[digit])

print("I am not a human.  Proof one:  %d" % totalone)
print("                   Proof half: %d" % totalhalf)