#Problem9
#find pythagorean triplet where a + b + c = 1000

def pythag_check(a, b):
	c = (a*a + b*b) ** 0.5
	#print(c)
	if c == int(c):
		return True
	return False

def pythag_triplet(k):
	for i in range(1,k-1):
		for j in range(1,k-i):
			if pythag_check(i,j):
				c = int((i*i + j*j) ** 0.5)
				if i + j + c == k:
					return i+j+c, i, j, c, i*j*c
	return False



print(pythag_check(3, 4))
print(pythag_triplet(1_000))