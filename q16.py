#-------------------------------------------------------------------------------
# Name:        Power Digit Sum

# Purpose:     2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#              What is the sum of the digits of the number 2^1000?

# Answer:      1366

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

EXPONENT = 1000
value = str(2 ** EXPONENT)
valSum = 0

for i in range(len(value)):
    valSum += int(value[i])

print valSum