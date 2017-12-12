print("Good evening.  Advent of Code 2017, Day 11.")
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_11.txt", "r")
inputLine = f.readline()
f.close()

row = 0
col = 0
minrow = 0
mincol = 0
maxcol = 0
maxrow = 0
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
    if row > maxrow:
        maxrow = row
    if row < minrow:
        minrow = row
    if col > maxcol:
        maxcol = col
    if col < mincol:
        mincol = col

print ("Hello world, I'm up and alive!")
print (row, col)
print (minrow, mincol)
print (maxrow, maxcol)