def quick_sort(nums):
	quick_sort_helper(nums, 0, len(nums)-1)

def quick_sort_helper(nums, firtst, last):
	if firtst < last:
		splitPoint = partition(nums, firtst, last)
		quick_sort_helper(nums, firtst, splitPoint-1)
		quick_sort_helper(nums, splitPoint+1, last)

def partition(nums, firtst, last):
	pivotValue = nums[firtst]
	left, right = firtst + 1, last
	done = False
	while not done:
		while left <= right and nums[left] <= pivotValue:
			left += 1
		while right >= left and nums[right] >=pivotValue:
			right -= 1
		if right < left:
			done = True
		else:
			nums[left], nums[right] = nums[right], nums[left]
	nums[firtst], nums[right] = nums[right], nums[firtst]
	return right

if __name__ == '__main__':
	nums = [3, 1, 5, 4, 2, 9, 8, 6, 0, 7]
	quick_sort(nums)
	print(nums)