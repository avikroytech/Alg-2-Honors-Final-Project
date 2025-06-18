import math
import time
import matplotlib.pyplot as plt

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

# Collect time measurements
sizes = list(range(1, 1001))
times = []
sqrt_n_curve = []

for n in sizes:
    test_list = list(range(n))
    target = n - 1  # Worst-case: last element

    start = time.perf_counter()
    jump_search(test_list, target)
    end = time.perf_counter()

    times.append(end - start)
    sqrt_n_curve.append(math.sqrt(n) * 1e-7)  # Scaled for comparison

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, times)
plt.xlabel('List Size (n)')
plt.ylabel('Time (seconds)')
plt.ticklabel_format(style='plain', axis='both')
plt.tight_layout()
plt.show()
