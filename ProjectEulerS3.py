#Problem3
#Find largest prime factor of 600_851_475_143

def prime_factor(number, factor_limit):
	c = number
	factors = []
	for i in range(2,factor_limit):
		if c % i == 0:
			factors.append(i)
			c = c // i
			#print(c,i)
	return factors
		#if c // list_of_primes[i] == 0:
		#	print(c,i)

def better_prime_factor(number):
	largest_factor = 1
	c = number
	i = 2

	while c > 1:
		if c % i == 0:
			largest_factor = i
			c = c // i
		i += 1
	print(largest_factor)
	
better_prime_factor(600_851_475_143)
#better_prime_factor(194)
#better_prime_factor(323)
#list_of_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349]

#print(list_of_primes[13])

print(prime_factor(600851475143, 1_000_000))
print(prime_factor(1234567890, 1_000_000))
