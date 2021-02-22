from compare_permutations import compare_string

def find_permutations(first, second):
	longer = first if len(first) > len(second) else second
	shorter = first if len(first) < len(second) else second
	window = len(shorter) - 1
	end = len(longer) - 1 
	start = 0 
	positions = []

	while start < end - 2:
		sub_string = longer[start: window + 1]
		found_permutation = compare_string(shorter, sub_string)

		if found_permutation:
			positions.append((start, window))

		start += 1
		window += 1

	return positions

def main():
	first_string = 'cbabadcbbabbcbabaabccbabc'
	second_string = 'abbc'  

	results = find_permutations(first_string, second_string)

	for a, b in results:
		print(first_string[a: b + 1])

main()
