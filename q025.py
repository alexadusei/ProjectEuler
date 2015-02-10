#-------------------------------------------------------------------------------
# Name:        1000-digit Fibonacci Number

# Purpose:     The Fibonacci sequence is defined by the recurrence relation:
#              F1 = 1
#              F2 = 1
#              F3 = 2
#              F4 = 3
#              F5 = 5
#              F6 = 8
#              F7 = 13
#              F8 = 21
#              F9 = 34
#              F10 = 55
#              F11 = 89
#              F12 = 144
#              The 12th term, F12, is the first term to contain three digits.
#              What is the first term in the Fibonacci sequence to contain 1000
#              digits?
#
# Answer:      4782

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

# term1 and term2 are current values of n1 and n2. So we start 'i' at 2
n1, n2, i, isGoal = 1, 1, 2, False

while not isGoal:
    i += 1
    n1, n2 = n2, (n1+n2)
    isGoal = len(list(str(n2))) == 1000

print i