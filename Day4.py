#import math
#import itertools
#import solveadventquickly....nah, let's at least put a tiny bit of effort in.

print("Good evening.  Advent of Code 2017, Day 4.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_4.txt", "r")
inputfile = f.readlines()
f.close()

valid1 = 0
valid2 = 0

for passphrase in inputfile:
    # Make two copies of the set of passwords
    passwords = passphrase.strip("\n").split(" ")
    securewords = passwords
    # First check: Are words unique?  Sort them for cheap comparison.
    sortwords = sorted(passwords)
    isgood = 1
    for itr in range(1, len(sortwords)):
        if(sortwords[itr] == sortwords[itr-1]):
            isgood = 0
            break   # If one thing's bad, the phrase is a loss.
    valid1 = valid1 + isgood    # Glorified +1.
    if isgood == 0:
        continue    # Fails part 2 anyway.
    
    # Sort each word.
    for itr in range(0, len(securewords)):
        securewords[itr] = sorted(securewords[itr])
    # Now each word is its least interesting acronym.  Any duplicates?
    securewords = sorted(securewords)
    for itr in range(1, len(securewords)):
        if(securewords[itr] == securewords[itr-1]):
            isgood = 0
            break
    if isgood > 0:
        valid2 = valid2 + isgood
        continue
    
# Report the results!
print("There are %d valid passphrases." % valid1)
print("There are %d very valid passphrases." % valid2)
    