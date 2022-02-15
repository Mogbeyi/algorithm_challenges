def find_start(arr, target):
	if arr[0] == target:
		return 0

	low, high = 0, len(arr) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = arr[mid]

		if guess == target and arr[mid - 1] < target:
			return mid
		elif guess < target:
			low = mid + 1
		else:
			high = mid - 1

	return None

def find_last(arr, target):
	if arr[-1] == target:
		return len(arr) - 1

	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2
		guess = arr[mid]

		if guess == target and arr[mid + 1] > target:
			return mid
		elif guess > target:
			right = mid - 1
		else:
			left = mid + 1

	return None


def find_first_and_last(arr, target):
	if len(arr) == 0:
		return [-1, -1]

	first = find_start(arr, target)
	last = find_last(arr, target)

	if first == None and last == None:
		return [-1, -1]
	elif first == None:
		return [last, last]
	elif last == None:
		return [first, first]
	else:
		return [first, last]
