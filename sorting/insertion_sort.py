def insertion_sort(nums):
	for index in range(1, len(nums)):
		curValue = nums[index]
		pos = index
		while pos > 0 and nums[pos-1] > curValue:
			nums[pos] = nums[pos-1]
			pos -= 1
		nums[pos] = curValue
	
if __name__ == '__main__':
	nums = [1,3,5,7,6,2,4,9,8]
	insertion_sort(nums)
	print(nums)