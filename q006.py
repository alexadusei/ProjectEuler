#-------------------------------------------------------------------------------
# Name:        Sum Square Difference

# Purpose:     The sum of the squares of the first ten natural numbers is,
#              1^2 + 2^2 + ... + 10^2 = 385. The square of the sum of the first
#              ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
#              Hence the difference between the sum of the squares of the first
#              ten natural numbers and the square of the sum is 3025-385 = 2640.
#              Find teh difference between the sum of the squares of the first
#              one hundred natural numbers and the square of the sum.

# Answer:      25164150

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

NATURAL_NUMS = 100
sumSquares = 0

for i in range(1, NATURAL_NUMS+1):
    sumSquares += i**2

print sum(range(1 , NATURAL_NUMS+1))**2 - sumSquares