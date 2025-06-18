from measure import measure_runtime_across_range, measure_search_runtime
from mplt import plot_func_runtimes

from runtime_funcs.constant import constant
from runtime_funcs.linear import linear
from runtime_funcs.quadratic import quadratic
from runtime_funcs.cubic import cubic
from runtime_funcs.exponential import exponential
from runtime_funcs.log import log

from algorithms.search.linearsearch import linear_search
from algorithms.search.binarysearch import binary_search
from algorithms.search.ternarysearch import ternary_search
from algorithms.search.jumpsearch import jump_search

# Get a list of runtimes for each val n and plot them
runtimes = measure_search_runtime(jump_search, 1, 1000)
plot_func_runtimes(runtimes, "LINEAR SEARCH")