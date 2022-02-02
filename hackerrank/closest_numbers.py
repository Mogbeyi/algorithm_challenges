'''
3. Find the pairs
4. Convert pairs to array
5. Return array
'''

def closestNumbers(arr):
	sorted_arr = sorted(arr)
	min_diff = abs(sorted_arr[0] - sorted_arr[1])
	result = []

	for i in range(len(arr) - 1):
		diff = abs(sorted_arr[i] - sorted_arr[i + 1])
		if diff < min_diff:
			min_diff = diff

	for i in range(len(arr) - 1):
		first = sorted_arr[i]
		second = sorted_arr[i + 1]
		diff = abs(first - second)

		if diff == min_diff:
			result.append(first)
			result.append(second)

	return result

print(closest_numbers([5,2,3,4,1]))



