# Simple function that runs in O(2^n) time complexity
def exponential(n):
	sum = 0
	for i in range(2 ** n):
		sum += i

	return sum