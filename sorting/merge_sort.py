def merge_sort(nums):
	if len(nums) > 1:
		mid = len(nums) // 2
		lefthalf, righthalf = nums[:mid], nums[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)
		i, j, k = 0, 0, 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				nums[k] = lefthalf[i]
				i += 1
			else:
				nums[k] = righthalf[j]
				j += 1
			k += 1
		while i < len(lefthalf):
			nums[k] = lefthalf[i]
			i += 1
			k += 1
		while j < len(righthalf):
			nums[k] = righthalf[j]
			j += 1
			k += 1

if __name__ == '__main__':
	nums = [1, 3, 5, 4, 2, 0, 7, 6, 9, 8]
	merge_sort(nums)
	print(nums)

