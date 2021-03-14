def upper_lower_stock(arr):
	minimum_value = get_value(arr, lambda x, y: x < y) 
	maximum_value = get_value(arr, lambda x, y: x > y) 
	total = 0

	for element in arr:
		if element != minimum_value or element != maximum_value:
			total += element

	return total / len(arr) 

def get_value(arr, func):
    result = arr[0]

    for element in arr:
        if func(element, result): 
            result = element

    return result

print(upper_lower_stock([1,2,3,4]))
