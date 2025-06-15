import matplotlib.pyplot as plt

def plot_func_runtimes(runtimes, func_type):
	y_vals = []
	x_vals = []

	print(f"----------- {func_type} RUNTIMES -----------")
	for n, runtime in runtimes:
		y_vals.append(round(runtime, 10))
		x_vals.append(n)
		print(f"|-- n: {n} --- runtime: {runtime:.10f} --|")
		
	plt.plot(x_vals, y_vals)
	plt.xlabel("n")
	plt.ylabel("Runtime (s)")
	plt.ticklabel_format(style='plain', axis='both')
	plt.show()