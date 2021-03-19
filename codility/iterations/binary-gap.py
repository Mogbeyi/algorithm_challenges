def convert_to_binary(N):
	binary_value = ''

	while (N):
		if N == 1:
			binary_value += '1' 
		elif N % 2 == 0:
			binary_value += '0' 
		else:
			binary_value += '1' 

		N = N // 2

	return binary_value[::-1]

def solution(N):
	binary_value = convert_to_binary(N)
	one_positions = get_one_positions(binary_value)
	longest_binary_gap = 0

	for i in range(len(one_positions) - 1):
		difference = abs(one_positions[i] - one_positions[i + 1])
		if difference > longest_binary_gap: 
			longest_binary_gap = difference 

	return 0 if longest_binary_gap == 0 else longest_binary_gap - 1


def get_one_positions(value):
	return [i for i in range(len(value)) if value[i] == '1']

