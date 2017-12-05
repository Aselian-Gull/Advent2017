import math
import hashlib

print("Good morning, world.  Welcome to the Advent of Code, 2017.")

mylist = []
mylist.append(5.0)
mylist.append(4)
mylist.append("Another world.")
mylist.append(math.pi)
mylist.append(1 + 1j)
mylist.append(mylist[4] * (1 - 1j))

for x in mylist:
    print(x)
    
print(mylist[2].upper()[::2])

f = open("/home/smacgil/Development/Advent/input2015_1.txt", "r")
santadirs = f.read()
f.close()

floor = 0
idx = 0
sundwell = 1

for direc in santadirs:
    if direc == "(":
        floor += 1
    elif direc == ")":
        floor -= 1
    idx += 1
    if(floor < 0 and sundwell > 0):
        print ("Basement entered on step %d" % idx)
        sundwell = 0

print ("Ended on floor %d" % floor)

key = "iwrupvqb"
for val in range(0, 1000000):
    hashkey = "%s%d" % (key, val);
    hasher = hashlib.md5()
    hasher.update(hashkey.encode())
    hashed = hasher.hexdigest()
    if(hashed[0:5:1] == "00000"):
        print(val)
        break

print ("Happy Holidays.")
        