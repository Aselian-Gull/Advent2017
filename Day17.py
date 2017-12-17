print ("TODO: insert witty opening line.  Advent of Code 2017, Day 17.")

# Key value.
keyval = 382
year = 2017

locked = [0]

curPos = 0

# Compute the list up to this point.
for val in range(year):
    newPos = (curPos + keyval) % (val + 1)
    locked.insert(newPos+1, (val+1))
    curPos = newPos + 1

# Find the item after 2017.
for item in range(len(locked)):
    if locked[item] == year:
        print(locked[item+1])
        break

# Rather than trouble ourselves with actually maintaining the list after this
# let's just spit out every item we insert after 0.
for val in range(year, 50000000):
    newPos = (curPos + keyval) % (val + 1)
    if (newPos == 0):
        print(val+1)
    curPos = newPos + 1
    
print ("And that's how we save Christmas.")