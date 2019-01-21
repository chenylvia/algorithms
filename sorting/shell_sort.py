def shell_sort(nums):
	sublistCount = len(nums) // 2
	while sublistCount > 0:
		for start in range(sublistCount):
			gap_insertion(nums, start, sublistCount)
			print('after increments of size', sublistCount, 'the list is', nums)
		sublistCount //= 2

def gap_insertion(nums, start, gap):
	for i in range(start+gap, len(nums), gap):
		curValue = nums[i]
		pos = i
		while pos >= gap and  nums[pos-gap] > curValue:
			nums[pos] = nums[pos-gap]
			pos -= gap
		nums[pos] = curValue

if __name__ == '__main__':
	nums = [1, 3, 5, 4, 2, 7, 6, 9, 8, 0]
	shell_sort(nums)
	print(nums)
	


	