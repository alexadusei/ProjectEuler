#-------------------------------------------------------------------------------
# Name:        Large Sum

# Purpose:     Work out the first first ten digits of the sum of the following
#              one-hundred 50-digit numbers.

# Answer:      5537376230

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

# Helper function to read large number from textfile
def readNums():
    file = open("q013.txt")
    nums = []

    for line in file:
        line = line.strip()
        nums += [int(line)]

    return nums

numbers = readNums()
print str(sum(numbers))[:10]