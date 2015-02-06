#-------------------------------------------------------------------------------
# Name:        Largest Prime Factor

# Purpose:     The prime factors of 13195 are 5, 7, 13 and 29. What is the
#              largest prime factor of the number 600851475143?
#
# Answer:

# Author:      Alex Adusei
#-------------------------------------------------------------------------------


def primeNumbers():
    RANGE = 100
    primes = []
    i = 2

    while len(primes) < RANGE: #for i in range(2, RANGE+1):
        isPrime = True

        for k in range(2, i):
            if i % k == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(i)
        i += 1

    return primes

primes = primeNumbers()
target = 12
isfactor = False




