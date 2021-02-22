def binary_search(arr, target):
	high = len(arr) - 1
	low = 0

	while (low <= high):
		middle = (low + high) // 2
		guess = arr[middle]

		if guess == target:
			return True
		elif arr[middle] > target:
			high = middle - 1
		else:
			low = middle + 1

	return False
	
def sorted_array(first, second):
	count = 0
	start = 0

	for i in range(len(first) - 1):
		found = binary_search(second, first[i])
		if found:
			count += 1
			start = i
			i = start

	return count

assert sorted_array([13, 27, 35, 40, 49, 55, 59], [17, 35, 39, 40, 55, 58, 60]) == 3
