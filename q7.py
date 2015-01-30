#-------------------------------------------------------------------------------
# Name:        1001st Prime

# Purpose:     By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we
#              can see that the 6th prime is 13. What is teh 10001st prime
#              number?
#
# Answer:      104743

# Author:      Alex Adusei
#-------------------------------------------------------------------------------

#TODO: Find all prime numbers in given range, put in list
#TODO: With new loop, check if number is divisible by smallest prime number,
#      if so, start process again with same number. If not, go up. if num >= target,
#      stop

RANGE = 10001
primes = []
i = 2

print "Working solution..."

while len(primes) < RANGE: #for i in range(2, RANGE+1):
    isPrime = True

    for k in range(2, i):
        if i % k == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(i)
    i += 1

print primes[-1]
