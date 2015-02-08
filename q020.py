#-------------------------------------------------------------------------------
# Name:        Factorial Digit Sum

# Purpose:     n! means n x (n-1) x ... x 3 x 2 x 1 For example,
#              10! = 10 x 9 x ... x 3 x 2 x 1 = 368800, and the sum of digits
#              in the number 10! is 3 + 6 + 8 + 8 + 0 + 0 = 27. Find the sum of
#              the digits in the number 100!
#
# Answer:      648

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

VALUE = 100
factorial = 1
sumFactorial = 0

for i in range(VALUE):
    factorial *= VALUE - i;

for digit in (str(factorial)):
    sumFactorial += int(digit)

print sumFactorial