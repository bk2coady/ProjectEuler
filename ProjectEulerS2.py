#Problem2
#Find the even Fibonacci numbers

def fib_counter(a,b,max_fib_limit):
	sum_even_fib = 0
	c = 0
	if a % 2 == 0:
		c = c + a
	if b % 2 == 0:
		c = c + b
	#print(a)
	#print(b)
	while(c < max_fib_limit):
		if c % 2 == 0:
			sum_even_fib += c
		#print(c)
		c = a + b
		a = b
		b = c
	return sum_even_fib


print(fib_counter(1,2,4_000_000))
