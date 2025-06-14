from measure import measure_runtime_across_range
from mplt import plot_func_runtimes

# A simple linear function
def linear(n):
    sum = 0
    for i in range(n):
        sum += 1
    return sum

runtimes = measure_runtime_across_range(linear, 1, 10000)
plot_func_runtimes(runtimes, "LINEAR")
    
