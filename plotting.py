from measure import measure_runtime_across_range
from mplt import plot_func_runtimes

from runtime_funcs.constant import constant
from runtime_funcs.linear import linear
from runtime_funcs.quadratic import quadratic
from runtime_funcs.cubic import cubic
from runtime_funcs.exponential import exponential
from runtime_funcs.log import log

# Get a list of runtimes for each val n and plot them
runtimes = measure_runtime_across_range(log, 1, 100000)
plot_func_runtimes(runtimes, "CONSTANT")