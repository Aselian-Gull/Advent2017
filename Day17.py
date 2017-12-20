print ("TODO: insert witty opening line.  Advent of Code 2017, Day 17.")

# Key value.
keyval = 382
year = 2017

locked = [0]

curPos = 0

# Compute the list up to this point.
for val in range(year):
    curPos = (curPos + keyval) % (val + 1) + 1
    locked.insert(curPos, (val+1))

# Find the item after 2017.
for item in range(len(locked)):
    if locked[item] == year:
        print("Item after 2017 is %d" % locked[item+1])
        break

# Rather than trouble ourselves with actually maintaining the list after this
# let's just spit out every item we insert after 0.
for val in range(year, 50000000):
    curPos = (curPos + keyval) % (val + 1) + 1
    if (curPos == 1):   # Right after zero
        print("Inserted %d" % (val+1))
    
print ("And that's how we save Christmas.")