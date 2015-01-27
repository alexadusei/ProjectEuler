#-------------------------------------------------------------------------------
# Name:        Smallest Multiple

# Purpose:     2520 is the smallest number that can be divided by each of the
#              numbers from 1 to 10 without any remainder. WHat is the smallest
#              positive number that is evenly divisible by all numbers from
#              1 to 20?

# Answer:

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

smallestNum = 0
num = 4100000

while True:
    isDivisible = []
    for i in range(1, 11):
        isDivisible.append(False)

        if num % i == 0:
            isDivisible[-1] = True
##        print num

    print num, smallestNum, isDivisible

    if False not in isDivisible:
        smallestNum = num
        break
    num += 1

print smallestNum, num