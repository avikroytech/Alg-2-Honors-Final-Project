import time

# Measure runtime of a function by passing it and n
def measure_runtime(function, n):
	start_time = time.perf_counter()
	function(n)
	end_time = time.perf_counter()
	runtime = end_time - start_time
	return runtime

# Runs a function and measures runtime across range with start and end (inclusive) values
def measure_runtime_across_range(function, start, end):
	runtimes = []

	for i in range(start, end + 1):
		runtime = measure_runtime(function, i)
		runtimes.append((i, runtime))

	return runtimes

