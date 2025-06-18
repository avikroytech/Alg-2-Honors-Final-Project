import time
import random

# Measure runtime of a function by passing it and n
def measure_runtime(function, n):
	start_time = time.perf_counter()
	function(n)
	end_time = time.perf_counter()
	runtime = end_time - start_time
	return runtime

# Measure runtime of a search
def measure_search(function,input,target):
	start_time = time.perf_counter()
	function(input,target)
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

# Runs a search function and measures runtime
def measure_search_runtime(function, start, end):
	runtimes = []

	for i in range(start,end+1):
		input_list = list(range(i))
		start = time.perf_counter()
		function(input_list, i-1)
		end = time.perf_counter()

		runtimes.append((i, end-start))

	return runtimes

# Runs a sort function on an unsorted list and measures runtime
def measure_sort_runtime(function, start, end):
	runtimes = []

	for i in range(start, end+1):
		unsorted_list = list(range(1,i+1))
		random.shuffle(unsorted_list)

		start = time.perf_counter()
		function(unsorted_list)
		end = time.perf_counter()

		runtimes.append((i, end-start))

	return runtimes