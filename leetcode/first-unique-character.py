from collections import Counter

def first_unique_character(s):
	letter_freq = Counter(s)

	for i, char in enumerate(s):
		if letter_freq[char] == 1:
			return i

	return -1
