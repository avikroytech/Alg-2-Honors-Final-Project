from measure import measure_runtime

# Simple function that runs in O(2^n) time complexity
def exponential(n):
	sum = 0
	for i in range(2 ** n):
		sum += i

	return sum

runtime = measure_runtime(exponential, 5)
print(f"Runtime: {runtime:.6f} seconds")