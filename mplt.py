import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.show()

def plot_func_runtimes(runtimes, func_type):
	y_vals = []
	x_vals = []

	print(f"----------- {func_type} RUNTIMES -----------")
	for n, runtime in runtimes:
		y_vals.append(runtime)
		x_vals.append(n)
		print(f"|-- n: {n} --- runtime: {runtime:.10f} --|")
		
	plt.plot(x_vals, y_vals)
	plt.xlabel("n")
	plt.ylabel("Runtime")
	plt.show()