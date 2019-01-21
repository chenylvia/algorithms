def bubble_sort(nums):
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
	nums = [1,3,5,4,6,2]
	bubble_sort(nums)
	print(nums)
