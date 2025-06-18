# Simple implementation of binary search
def binary_search(arr, target, high, low):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			return binary_search(arr, target, low, mid - 1)
		else:
			return binary_search(arr, target, high, mid + 1)
	else:
		return False