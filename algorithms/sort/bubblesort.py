import random

# Simple implementation of bubble sort
def bubble_sort(arr):
	n = len(arr)
	
	for i in range(n):
		swapped = False

		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break