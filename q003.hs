module Q003 where

{- 	Name: 	 Largest Prime Factor

	Purpose: The primes factors of 13195 are 5, 7, 13 and 29.
			 What is the largest prime factor of the number 600851475143?

	Answer:  6857

	Author: Alex Adusei 
-}

num = 600851475143 

-- Function that takes value to determine smallest prime factor 
start n = largestPrimeFactor n (intRoot n)

-- finds smallest factor of n >= f
largestPrimeFactor n f
	| (mod n f == 0) && isPrime f = f
	| otherwise = largestPrimeFactor n (f-1)

-- Auxiliary function checking if a number is prime
isPrime :: Integer -> Bool
isPrime n = null [fact | fact <- [2..(intRoot n)], mod n fact == 0]

intRoot n = floor (sqrt (fromIntegral n))