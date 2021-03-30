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
    prev = 0
    next = 0
    maximum = 0

    for i, value in enumerate(binary_value):
        if value == '1':
            next = i
            maximum = next - prev if next - prev > maximum else maximum
            prev = next

    return maximum - 1

