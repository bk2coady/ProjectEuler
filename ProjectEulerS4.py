#Problem4
#Find largest palindrome made from the product of two 3-digit numbers

def split_number(number):
	a = number
	digits = []
	while (a >= 1):
		digits.insert(0,a % 10)
		#print(a % 10)
		a = a // 10
	return digits

def is_palindrome_number(number):
	list_of_digits = split_number(number)
	for i in range(len(list_of_digits)//2):
		#print(list_of_digits[i], list_of_digits[-i-1])
		if list_of_digits[i] != list_of_digits[-i-1]:
			return False
	return True

def find_max_palindrome(start_value, end_value):
	max_palindrome = [0,0,0]
	for i in range(start_value, end_value):
		for j in range(i, end_value):
			if is_palindrome_number(i*j):
				print(i,j, i*j)
				if i*j > max_palindrome[0]:
					max_palindrome[0] = i*j
					max_palindrome[1] = i
					max_palindrome[2] = j
					#print(i,j) 
	return max_palindrome



#digits = 123321
#print(is_palindrome_number(digits))

#note: no sense checking smaller than 900 in order to find largest product of 3-digit numbers
print(find_max_palindrome(800, 1000))
