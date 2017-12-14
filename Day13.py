print("This just went badly.  Advent of Code 2017, Day 13.")
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_13.txt", "r")
inputLines = f.readlines()
f.close()

depths = {}
numScans = 0
for line in inputLines:
    tokens = line.strip('\n').split(':')
    depths[int(tokens[0])] = int(tokens[1])
    numScans = max(numScans, int(tokens[0]))

# Right.  Calculate the severity for starting immediately.
severity = 0
for col in depths:
    depth = depths[col]
    cycle = 2 * (depth - 1)
    if depth != 0 and col % cycle == 0:
        severity = severity + (depth * col)
        
print ("Severity is equal to %d" % severity)

# Now just brute-force it.  Can we do better?
for tryDelay in range(0, 10000000):
    canPass = 1
    for idx in depths:
        depth = depths[idx]
        cycle = 2 * (depth - 1)
        if ((tryDelay + idx) % cycle) == 0:
            canPass = 0
            break
    if canPass > 0:
        print("If we wait %d picoseconds, we'll make it through." % tryDelay)
        break