#Problem1

#Find sum of all numbers which are multiples of more than one value (ie 3 and 5)
#remember to not double-count numbers that are multiples of both 3 and 5 (ie multiples of 15)

def sumofmultiples(value, max_value):
	total = 0
	for i in range(1,max_value):
		if i % value == 0:
			#print(i)
			total = total+i
			#print(total)
	return total

upto = 1000
cumulative_total = sumofmultiples(3,upto) + sumofmultiples(5,upto) - sumofmultiples(15,upto)

print(cumulative_total)
