def radix_sort(arr):
	digit = len(str(max(arr)))

	for i in range(digit):
		temp = [[] for _ in range(10)]
		for num in arr:
			pos = int(num // (10 ** i) % 10)
			temp[pos].append(num)
		arr = [y for x in temp for y in x]

	return arr

if __name__ == '__main__':
	arr = [23, 45, 4, 674, 1357, 5, 9, 367, 3261]
	print(radix_sort(arr))