print("Good evening.  Advent of Code 2017, Day 9.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_9.txt", "r")
inStream = f.read()
f.close()

isJunk = 0      # Indicates whether current characters are 'garbage'.
isCancel = 0    # Indicates whether the next character should be cancelled.
nest = 0        # Current recursion level.
total = 0       # Total for all nested groups.
garbage = 0     # How many junk characters there were, not including cancellations.

for cur in inStream:
    if isCancel > 0:    # Previous character cancels this one.
        isCancel = 0
    elif cur == '!':    # Cancel the next character.
        isCancel = 1
    elif isJunk > 0:    # We're currently handling garbage characters.
        if cur == '>':  # Stop handling them..
            isJunk = 0
        else:           # Add to the count.
            garbage = garbage + 1
    elif cur == '<':    # Entering garbage mode.
        isJunk = 1
    elif cur == '{':    # Going one level deeper.
        nest = nest + 1
    elif cur == '}':    # Recognize a group at the current level.
        total = total + nest
        nest = nest - 1
    # Fallback: Do nothing.
    
    
print ("The total ranking of nested groups is %d" % total)
print ("The number of garbage characters was %d" % garbage)