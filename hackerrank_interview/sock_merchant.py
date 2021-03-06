# def sock_merchant(n, arr):
# 	start_index = 0
# 	stop_index = n - 1
# 	no_of_pairs = 0
# 	sorted_array = sorted(arr)

# 	while start_index < stop_index:
# 		if sorted_array[start_index] == sorted_array[start_index + 1]:
# 			no_of_pairs += 1
# 		start_index += 2

# 	return no_of_pairs


def sockMerchant(n, ar):
    array_set = set()
    count = 0
    
    for elem in ar:
        if elem in array_set:
            array_set.remove(elem)
            count += 1
        else:
            array_set.add(elem)
            
    return count


print(sockMerchant(7, [1,2,1,2,1,3,2]))
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
