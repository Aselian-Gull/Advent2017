print("Good evening.  Advent of Code 2017, Day 11.")
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_11.txt", "r")
inputLine = f.readline()
f.close()

row = 0
col = 0
maxdist = 0
def hexDist(row, col):
    tempdist = abs(col)
    if abs(col) < abs(row):
        tempdist = tempdist + (abs(row) - abs(col)) / 2
    return tempdist

inputTokens = inputLine.strip('\n').split(',')

for token in inputTokens:
    if token == "n":
        row += 2
    elif token == "s":
        row -= 2
    elif token == "se":
        row -= 1
        col += 1
    elif token == "sw":
        row -= 1
        col -= 1
    elif token == "ne":
        row += 1
        col += 1
    elif token == "nw":
        row += 1
        col -= 1
    maxdist = max(maxdist, hexDist(row, col))

print ("Hello world, I'm up and alive!")
print ("%d, %d has a distance of %d" % (row, col, hexDist(row, col)))
print ("The furthest we got was %d" % maxdist)