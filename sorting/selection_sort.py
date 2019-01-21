def seletion_sort(nums):
	for i in range(len(nums)-1, 0, -1):
		maxIndex = 0
		for j in range(1, i+1):
			if nums[j] > nums[maxIndex]:
				maxIndex = j
		nums[i], nums[maxIndex] = nums[maxIndex], nums[i]

if __name__ == '__main__':
	nums = [1, 3, 5, 6, 4, 2, 8, 9, 7]
	seletion_sort(nums)
	print(nums)