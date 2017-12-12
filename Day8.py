#import solveadventquickly....oh wait, I have to finish writing it.

print("Good evening.  Advent of Code 2017, Day 8.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_8.txt", "r")
inputfile = f.readlines()
f.close()

print ("There is no hope.  No solution.  Only despair.")

registers = {}

runMax = 0
runName = ""
finalMax = 0
finalName = ""

for instruct in inputfile:
    instruct = instruct.rstrip() # Say farewell to newline characters.
    tokens = instruct.split(" ")
    comp = tokens[5]
    test = registers.get(tokens[4], 0)
    newval = registers.get(tokens[0], 0)
    if(tokens[1] == "inc"):
        newval = newval + int(tokens[2])
    else: #dec
        newval = newval - int(tokens[2])
    
    setval = 0
    if(comp == "<" and test < int(tokens[6])):
        setval = 1
    if(comp == ">" and test > int(tokens[6])):
        setval = 1
    if(comp == "<=" and test <= int(tokens[6])):
        setval = 1
    if(comp == ">=" and test >= int(tokens[6])):
        setval = 1
    if(comp == "==" and test == int(tokens[6])):
        setval = 1
    if(comp == "!=" and test != int(tokens[6])):
        setval = 1
    if setval > 0:
        registers[tokens[0]] = newval
        if newval > runMax:
            runMax = newval
            runName = tokens[0]
        
for reg in registers:
    if registers[reg] > finalMax:
        finalMax = registers[reg]
        finalName = reg
        
print ("The highest run-time value was %d in register %s" % (runMax, runName))
print ("The highest endstate value was %d in register %s" % (finalMax, finalName))
    