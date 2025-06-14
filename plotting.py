from measure import measure_runtime_across_range
from mplt import plot_func_runtimes

from runtime_funcs.constant import constant
from runtime_funcs.linear import linear
from runtime_funcs.quadratic import quadratic
from runtime_funcs.cubic import cubic

runtimes = measure_runtime_across_range(cubic, 1, 100)
plot_func_runtimes(runtimes, "CUBIC")