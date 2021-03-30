def first_unique_character(s):
	for i, char in enumerate(s):
		if char not in s[i + 1:]:
			return char

	return -1 


