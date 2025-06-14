from measure import measure_runtime_across_range
import matplotlib.pyplot as plt

# A simple linear function
def linear(n):
    sum = 0
    for i in range(n):
        sum += 1
    return sum

runtimes = measure_runtime_across_range(linear, 1, 10000)
y_vals = []
x_vals = []

print("----------- LINEAR RUNTIMES -----------")
for n, runtime in runtimes:
    y_vals.append(runtime)
    x_vals.append(n)
    print(f"|-- n: {n} --- runtime: {runtime:.10f} --|")
    
plt.plot(x_vals, y_vals)
plt.xlabel("n")
plt.ylabel("Runtime")
plt.show()
    
