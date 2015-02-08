#-------------------------------------------------------------------------------
# Name:        Largest Product in a Series

# Purpose:     The four adjacent digits in the 1000-digit number (provided in
#              textfile 'q008.txt')  that have the greatest product are
#              9 x 9 x 8 x 9 = 5832. Find the thirteen adjacent digits in the
#              1000-digit number that have the greatest product. What is the
#              value of this product?

# Answer:      23514624000

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

# Helper function to read large number from textfile
def readNums():
    file = open("q008.txt")
    nums = []

    for line in file:
        line = line.strip()
        for i in range (len(line)):
          nums += [int(line[i])]

    return nums

numbers = readNums()
currentSum = 0
DIGITS = 13

for i in range(len(numbers)):
    digitSum = 1

    if i < (len(numbers) - DIGITS):
        for k in range(DIGITS):
            digitSum *= numbers[i+k]

        if digitSum > currentSum:
            currentSum = digitSum

print currentSum