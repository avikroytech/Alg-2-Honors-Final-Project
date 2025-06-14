from measure import measure_runtime_across_range
from mplt import plot_func_runtimes

# A simple function that gives a constant runtime
def constant(n):
    return n
    
runtimes = measure_runtime_across_range(constant, 1, 10000)
plot_func_runtimes(runtimes, "CONSTANT")