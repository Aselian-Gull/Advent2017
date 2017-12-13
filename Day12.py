print("Good evening.  Advent of Code 2017, Day 12.")
        
# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_12.txt", "r")
inputLine = f.readlines()
f.close()

friends = []
for line in inputLine:
    tokens = line.strip('\n').split(' ')
    flist = []
    for token in tokens[2:]:
        flist.append(int(token.strip(',')))
    friends.append(flist)

progGroups = {}
def appendList(index, iToken):
    for value in friends[index]:
        if progGroups.get(value,0) == 0:
            progGroups[value] = iToken
            appendList(value, iToken)

token = 0
for idx in range(0, len(friends)):
    if progGroups.get(idx, 0) == 0:
        token = token + 1
        appendList(idx, token)

numInZero = sum( 1 for t in progGroups.values() if t == 1)

print("The number of items in the same group as program zero is %d" % numInZero)        
print("The number of program groups is %d" % token)

print ("Still, we're gonna shout it loud, even if the words seem meaningless...")