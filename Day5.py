#import math
#import itertools
#import solveadventquickly....nah, let's at least put a tiny bit of effort in.

print("Good evening.  Advent of Code 2017, Day 5.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_5.txt", "r")
inputfile = f.readlines()
f.close()

for hardmode in [0,1]:
    vals = []
    for word in inputfile:
        vals.append(int(word))
        
    pos = 0
    maxpos = len(vals)
    steps = 0
    
    while pos < maxpos and pos >= 0:
        delta = vals[pos]
        if(vals[pos] >= 3 and hardmode == 1):
            vals[pos] = vals[pos] - 1
        else:
            vals[pos] = vals[pos] + 1
        pos = pos + delta
        steps = steps + 1
        
    print ("Escaped in %d" % steps)
    