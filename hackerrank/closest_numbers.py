'''
3. Find the pairs
4. Convert pairs to array
5. Return array
'''

def closestNumbers(arr):
	sorted_arr = sorted(arr)
	min_diff = get_min_diff(sorted_arr)
	result = get_result(sorted_arr, min_diff)

	return result


def get_min_diff(sorted_arr):
	min_diff = abs(sorted_arr[0] - sorted_arr[1])

	for i in range(len(sorted_arr) - 1):
		diff = abs(sorted_arr[i] - sorted_arr[i + 1])
		if diff < min_diff:
			min_diff = diff

	return min_diff

def get_result(arr, min_diff):
	result = []

	for i in range(len(arr) - 1):
		first = arr[i]
		second = arr[i + 1]
		diff = abs(first - second)

		if diff == min_diff:
			result.append(first)
			result.append(second)

	return result

print(closestNumbers([5,2,3,4,1]))



