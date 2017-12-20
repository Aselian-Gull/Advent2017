print ("It's time to jump up in the air!  Advent of Code 2017, Day 20.")

# Open the file, and get the lines.
f = open("/home/smacgil/Development/Advent/input2017_20.txt", "r")
inputLines = f.readlines()
f.close()

posVec = []
velVec = []
accVec = []
distVec = []
deadVec = []
numVecs = len(inputLines)

for line in inputLines:
    vals = line.strip('\n').split(',')
    posVec.append([int(vals[0][3:]), int(vals[1]), int(vals[2][:-1])])
    velVec.append([int(vals[3][4:]), int(vals[4]), int(vals[5][:-1])])
    accVec.append([int(vals[6][4:]), int(vals[7]), int(vals[8][:-1])])
    distVec.append(9999999)
    deadVec.append(0)
    
closest = 0
for tstamp in range(1000):
    bestDist = distVec[closest]
    for particle in range(len(inputLines)):
        distVec[particle] = 0
        for dim in range(3):
            velVec[particle][dim] = velVec[particle][dim] + accVec[particle][dim]
            posVec[particle][dim] = posVec[particle][dim] + velVec[particle][dim]
            distVec[particle] = distVec[particle] + abs(posVec[particle][dim])
        
        if distVec[particle] < bestDist:
            bestDist = distVec[particle]
            closest = particle
    # Okay, find duplicates.
    destroyed = 0
    for alpha in range(numVecs):
        if deadVec[alpha] != 0:
            continue
        for beta in range(alpha+1, numVecs):
            if deadVec[beta] != 0:
                continue
            if posVec[alpha] == posVec[beta]:
                deadVec[alpha] = tstamp+1
                deadVec[beta] = tstamp+1
                destroyed = 1

print("Closest point in the 'long' run is %d" % closest)
print("Survivors number %d" % sum(1 for x in deadVec if x == 0))
print("This is what you get for calling in the brute squad.")
print("(I am the brute squad.)")