def repeated_string(s, n):
	count_of_a = s.count('a')
	quotient = n // len(s)
	remainder = n % len(s)

	return count_of_a * quotient if remainder == 0 else count_of_a * quotient + s[:remainder].count('a')

print(repeated_string('abcac', 10))
print(repeated_string('aba', 10))
print(repeated_string('a', 1000000000000))
