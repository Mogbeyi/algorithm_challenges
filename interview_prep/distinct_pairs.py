def form_hash_pair(arr, k):
	hash_pair = {}

	for key in arr:
		if key not in hash_pair:
			hash_pair[key] = 0
		else:
			hash_pair[key] += 1

	return hash_pair

def distinct_pairs(arr, k):
	pairs = []
	hash_of_pairs = form_hash_pair(arr, k)

	for first_pair in arr:
		second_pair = first_pair + k

		if second_pair in hash_of_pairs:
			pairs.append((first_pair, second_pair))

	return pairs 


def test():
    assert (1, 3) in distinct_pairs([1,7,5,9,2,12,3], 2)
    assert (3, 5) in distinct_pairs([1,7,5,9,2,12,3], 2)
    assert (7, 9) in distinct_pairs([1,7,5,9,2,12,3], 2)

test()




