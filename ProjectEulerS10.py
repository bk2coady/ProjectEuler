#Problem10
#Find the sum of primes below 2 million

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

def sum_primes_below_n(n):
	total = 0
	for i in range(2, n):
		if prime_check2(i):
			total += i
			#print(i, total)
	return total

def better_sieve(num):
	marked = [0] * num 	#make 2M 0s
	value = 3			#ignore 
	total = 2
	while value < num:
		if marked[value] == 0:
			total += value
			i = value**2
			while i < num:
				marked[i] = 1
				i += value
		value += 2
	return total

#print(sum_primes_below_n(2_000_000))
print(better_sieve(2_000_000))