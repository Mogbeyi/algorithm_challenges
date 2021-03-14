def upper_lower_stock(arr):
	minimum_value = get_min(arr)
	maximum_value = get_max(arr)
	total = 0

	for element in arr:
		if element != minimum_value or element != maximum_value:
			total += element

	return total / len(arr) 


def get_min(arr):
	result = arr[0]

	for element in arr:
	    if element < result: 
	        result = element

	return result

def get_max(arr):
	result = arr[0]

	for element in arr:
	    if element > result: 
	        result = element

	return result

print(upper_lower_stock([1,2,3,4]))