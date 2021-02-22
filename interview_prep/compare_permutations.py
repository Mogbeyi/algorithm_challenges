def form_hash(string):
    hash_string = {}

    for elem in string:
        if elem in hash_string:
            hash_string[elem] += 1
        else:
            hash_string[elem] = 1

    return hash_string

def compare_string(first, second):
	first_hash = form_hash(first)
	second_hash = form_hash(second)

	for char in first:
		if char not in second_hash:
			return False 
		elif first_hash[char] != second_hash[char]:
			return False

	return True 

