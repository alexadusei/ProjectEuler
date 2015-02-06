#-------------------------------------------------------------------------------
# Name:        Largest Palindrome Product

# Purpose:     A palindromic number reads the same both ways. The largest
#              palindrome made from the product of two 2-digit numbers is
#              9009 = 91 x 99. Find the largest palindrome made from the
#              product of two 3-digit numbers.

# Answer:      906609 = 913 x 993

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

def isPalindrome(string):
    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False

x1, x2 = 0, 0

for i in range(100, 1000):
    for k in range(100, 1000):
        if isPalindrome(str(i*k)) and (i*k) > (x1*x2):
            x1, x2 = i, k

print "Products:", x1, x2, "\nPalindrome:", x1*x2