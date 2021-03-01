def sorted_arr(first_array, second_array):
	first_pointer = 0
	second_pointer = 0
	max_arr_length = len(first_array) - 1
	count = 0

	while first_pointer < max_arr_length or second_pointer < max_arr_length:
		if first_array[first_pointer] == second_array[second_pointer]:
			count += 1
			first_pointer += 1
		elif first_array[first_pointer] < second_array[second_pointer]:
			first_pointer += 1
		else:
			second_pointer += 1


	return count

print(sorted_arr([13, 27, 35, 40, 49, 55, 59], [17, 35, 39, 40, 55, 58, 60]))
