print ("TODO: insert witty opening line.  Advent of Code 2017, Day 16.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_16.txt", "r")
inputLine = f.readline()
f.close()

danceMoves = inputLine.strip('\n').split(',')

initialdance = "abcdefghijklmnop"
dlen = 16
dance = initialdance[:]

# Okay.  Rather than actually do the moves, let's track where they wind up.
swaps = {}
for dancer in initialdance:
    swaps[dancer] = dancer # For tracking the letter swaps.
for i in range(0, 16):
    swaps[i] = i            # For tracking position swaps.
for move in danceMoves:
    if move[0] == 'p':
        codes = move[1:].split('/')
        swaps[codes[0]], swaps[codes[1]] = swaps[codes[1]], swaps[codes[0]]
    elif move[0] == 's': #spin
        spinlen = int(move[1:])
        for i in range(0, 16):
            swaps[i] = (swaps[i] + spinlen) % 16
    elif move[0] == 'x':
        indexes = move[1:].split('/')
        a, b = int(indexes[0]), int(indexes[1])
        for i in range(0, 16):
            if swaps[i] == a:
                swaps[i] = b
            elif swaps[i] == b:
                swaps[i] = a
                
# Now invert - currently swaps[a] = b means that b goes to a.
invSwaps = {v: k for k, v in swaps.items()}

dance = ""
for i in range(0, 16):
    dance = dance + invSwaps[initialdance[invSwaps[i]]]
print(dance)

# Now for ONE BILLION = 10^9
def tenfold(baseSwaps):
    newSwaps = {}
    for val in baseSwaps:
        temp = val
        for e in range(10):
            temp = baseSwaps[temp]
        newSwaps[val] = temp
    return newSwaps

billSwaps = invSwaps.copy()
for d in range(9):
    billSwaps = tenfold(billSwaps)

Bdance = ""
for i in range(0, 16):
    Bdance = Bdance + billSwaps[initialdance[billSwaps[i]]]
print(Bdance)

print ("@aselian-gull you really need to work on your wit")