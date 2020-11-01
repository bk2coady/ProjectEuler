def prime_check2(n):
	#initial easy checks for 2 and 3
	if n == 2:
		return True
	if n == 3:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	#used to check 6k +/- 1 for sqrt(n)

	step = 4
	root_n = int(n ** 0.5)+1
	i = 5
	
	while i < root_n:
		if n % i == 0:
			return False
		step = 6 - step
		i += step
		#print(i)
		
	return True

def nth_prime(n):
	#i counts nth prime number
	i = 1
	#j counts all numbers
	j = 2
	while i < n:
		#print(i, j)
		j += 1
		if prime_check2(j):
			#print(j)
			i += 1
	return j

print(nth_prime(10_001))