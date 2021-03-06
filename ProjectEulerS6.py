#Problem6
#Sum of squares minus square of sums for n numbers
#(sum(i to n))^2 - sum((i to n)^2) = n_answer

def sum_of_squares(n):
	return n*(n+1)*(2*n+1)//6

def square_of_sums(n):
	return (n*(n+1)//2)**2

print(square_of_sums(100) - sum_of_squares(100))