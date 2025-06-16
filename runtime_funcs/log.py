# Simple function to simulate O(log2(n))
def log(n):
	sum = 0
	while n > 1:
		n = n // 2
		sum += 1
	
	return sum