def binary_search(arr, item):
	left, right = 0, len(arr)-1
	while left <= right:
		mid = (left + right) // 2
		if item > arr[mid]:
			left = mid + 1
		elif item < arr[mid]:
			right = mid - 1
		else:
			return mid
	return -1