def sqrt2_binary(n):
	if n < 0:
		raise ValueError
	left, right = 0, n
	acc = 1e-20
	while left < right:
		mid = left + (right - left) / 2
		diff = abs(mid ** 2 - n)
		if diff <= acc:
			return mid
		else:
			if mid ** 2 > n:
				right = mid
			else:
				left = mid

if __name__ == '__main__':
	n = 8
	print(sqrt2_binary(n))
