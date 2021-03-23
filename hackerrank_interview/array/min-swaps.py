# def min_swaps(arr):
# 	minimum_swaps = 0
# 	sub_array = arr

# 	for i in range(len(arr)):
# 		print(sub_array)
# 		index_of_min_elem = find_min_index(sub_array)

# 		if not is_first_element(index_of_min_elem):
# 			swap(sub_array, index_of_min_elem)
# 			minimum_swaps += 1
# 			sub_array = arr[i:] 
# 		else:
# 			sub_array = arr[i:]

# 	return minimum_swaps

# def is_first_element(idx):
# 	return idx == 0

# def find_min_index(array):
# 	return array.index(min(array))

# def swap(array, idx):
# 	temp = array[0]
# 	array[0] = array[idx]
# 	array[idx] = temp

# print(min_swaps([1, 3, 5, 2, 4, 6, 7]))

def min_swaps(arr):
	minimum_swaps = 0

	
