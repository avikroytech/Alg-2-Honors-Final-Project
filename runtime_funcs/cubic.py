# Simple function that runs in O(n^3)
def cubic(n):
	sum = 0
	for i in range(n):
		for j in range(n):
			for k in range(n):
				sum += k
			sum += j
		sum += i
		
	return sum