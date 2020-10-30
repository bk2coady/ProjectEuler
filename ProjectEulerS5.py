#Problem5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

def arr_primes_below_n(n):
	arr = {2}
	for i in range(2, n):
		if i not in arr:
			if prime_check2(i):
				arr.add(i)
	arr = sorted(arr)
	return arr

def prime_factors(number):
	pfactors = {}
	c = int(number)
	i = 2

	while c >= 1 and i <= number:
		if c % i == 0:
			if i in pfactors:
				pfactors[i] += 1
			else:
				pfactors[i] = 1
			c = c // i
		else:
			i += 1
	#print(i,c)
	return pfactors


def problem5():

	arr = {}
	total = 1

	for k in range(1,21):
		c = prime_factors(k)
		
		#cycle through all prime factors of k
		for j in c:
			#if prime factor is in arr
			if (j in arr):
				
				#and if quantity of prime factor is greater than current total for that prime factor in arr
				if c[j] > arr[j]:

					#make the quantity of prime factor the new total
					arr[j] = c[j]

			#else put new prime factor into arr
			else:
				#note than any new prime factor in arr must show up as 1 the first time
				arr[j] = 1
				
	for i in arr:
		total *= i**arr[i]

	print(total)
	return total

problem5()