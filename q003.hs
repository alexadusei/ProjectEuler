module Q003 where

-- Auxiliary function to isPrime
hasFactorInRange :: Integer -> Integer -> Integer -> Bool
hasFactorInRange n low high
	| low > high 		= False
	| mod n low == 0 	= True
	| otherwise 		= hasFactorInRange n (low+1) high 

-- Auxiliary function to primesLeq
isPrime n 
	| n <= 1 	= False
	| otherwise = not (hasFactorInRange n 2 sqrtFloor)
	where
	-- sqrtFloor is the square root of n rounded down to an integer
	-- fromIntegral takes int and changes into integral (float)
	sqrtFloor = floor (sqrt (fromIntegral n))

-- First prime greater than or equal to n
firstPrimeGeq n
	| isPrime n = n
	| otherwise = firstPrimeGeq (n+1)

-- Prime less than or equal to n 
primesLeq n
	| n <= 1 	= 0
	| isPrime n = n
	| otherwise = primesLeq (n-1)

-- finds smallest factor of n >= f
smallestFactorStarting n f
	| mod n f == 0 = f
	| otherwise = smallestFactorStarting n (f-1)

greatestPrimeFactor :: Integer -> Integer
greatestPrimeFactor n
	| mod n (primesLeq n) == 0 = primesLeq n
	| otherwise = greatestPrimeFactor(n-1)
