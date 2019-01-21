def bubble_sort_tag(nums):
	tag = True
	for i in range(len(nums) - 1):
		for j in range(len(nums) - i - 1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				tag = False
		if tag:
			break

if __name__ == '__main__':
	nums = [1,3,5,4,6,2]
	bubble_sort_tag(nums)
	print(nums)