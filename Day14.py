print("Remember day 10?  That was fun.  For nostalgia...\n")
print("~   ~   ~")
from Day10 import knotHash
print("~   ~   ~")
print("\nNow the real challenge begins.  Advent of Code 2017, Day 14.")
# play MEGALOVANIA.mp3

# Open the file, and get the line or lines.  Kind of a gamble setting this up.
inputkey = "xlqgujun"
sz = 128 # Row/Column size.

hashKeys = []
for row in range(sz):
    hashKeys.append("%s-%d" % (inputkey, row))

used = 0
hashes = []
frag = []
mask = []
for key in hashKeys:
    bits = []
    initOut = [0] * sz
    hashed = knotHash(key)
    for bit in range(sz):
        if hashed & (1 << bit):
            used = used + 1
            bits.append(1)
        else:
            bits.append(0)
    hashes.append(hashed)
    frag.append(bits)
    mask.append(initOut)

print ("Total bits used: %d" % used)
    
def markMask(reg, data, out, y, x):
    if y >= sz or y < 0 or x >= sz or x < 0:
        return
    if data[y][x] == 0:
        return
    if out[y][x] != 0:
        return
    out[y][x] = reg
    markMask(reg, data, out, y+1, x)
    markMask(reg, data, out, y-1, x)
    markMask(reg, data, out, y, x+1)
    markMask(reg, data, out, y, x-1)
    
regions = 0
for row in range(sz):
    for col in range(sz):
        if frag[row][col] != 0 and mask[row][col] == 0:
            regions = regions + 1
            markMask(regions, frag, mask, row, col)
print("Contiguous defragged regions: %d" % regions)