#-------------------------------------------------------------------------------
# Name:        Multiple of 3 and 5
# Purpose:     If we list all the natural numbers below 10 that are multiples
#              of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
#              Find the summ of all the multiples of 3 or 5 below 1000
#
# Author:      Alex Adusei
#
# Created:     22-01-2015
#-------------------------------------------------------------------------------

import time

def main():
    sumMultiples = 0

    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sumMultiples += i

    print sumMultiples

#Answer: 233168
t = time.clock();
main()
print round(time.clock() - t, 6), "seconds process time"