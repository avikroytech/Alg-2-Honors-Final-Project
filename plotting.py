from measure import measure_runtime_across_range
from mplt import plot_func_runtimes

from constant import constant
from linear import linear
from quadratic import quadratic
from cubic import cubic

runtimes = measure_runtime_across_range(quadratic, 1, 10000)
plot_func_runtimes(runtimes, "QUADRATIC")