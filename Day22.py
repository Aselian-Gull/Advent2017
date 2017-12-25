print ("Moderately awake...  Advent of Code 2017, Day 22.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_22.txt", "r")
inputLines = f.readlines()
f.close()

middle = len(inputLines)
worldGrid = []
ws = 500
hs = int(ws / 2)
for row in range(ws + middle):
    worldLine = [0] * (ws + middle)
    if(row >= hs and row < hs + middle):
        for col in range(hs, hs + middle):
            c = inputLines[row-hs][col-hs]
            if c == '#':
                worldLine[col] = 2
            elif c == '.':
                worldLine[col] = 0
    worldGrid.append(worldLine)

for stage in [0, 1]:
    # Calculate our parameters.
    infectRate = 2 - stage # Go 0 -> 2 -> 0 first run, 0 -> 1 -> 2 -> 3 second.
    iterations = 10000 * (1 + (999 * stage)) # 10k first run, 10M second.
    
    # d: 0 down, 1 left, 2 up, 3 right
    d = 2               # Start facing up.
    infectBursts = 0    # Reset the number of infected.
    grid = [row.copy() for row in worldGrid] # Deep copy the initial state. 
    posX = int(hs + (middle / 2))   # Start in the middle.
    posY = posX
    
    for t in range(iterations):
        if(posY >= ws or posX >= ws or posY < 0 or posX < 0):
            print((posX, posY))
            break
        curState = grid[posY][posX]
        if curState == 3: # Flagged : reverse
            d = (d + 2) % 4
        elif curState == 2: # Infected: Turn right
            d = (d + 1) % 4
        elif curState == 0: # 0 = Clean : turn left
            d = (d + 3) % 4
        grid[posY][posX] = (curState + infectRate) % 4
        
        if grid[posY][posX] == 2: # We just infected this.
            infectBursts = infectBursts + 1
        if d == 0:
            posY = posY + 1
        elif d == 1:
            posX = posX - 1
        elif d == 2:
            posY = posY - 1
        elif d == 3:
            posX = posX + 1
    
    print("Run %d: Running %d steps, incrementing infection by %d, resulted in infecting %d nodes"
           % (stage, iterations, infectRate, infectBursts))
    
print("There have been worse decisions.")