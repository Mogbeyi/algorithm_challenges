def recursive_recurence(string):
	if len(string) == 0:
		return -1
	elif string[0] in string[1:]:
		return string[0]

	return recursive_recurence(string[1:])


print(recursive_recurence('ABCAB'))
print(recursive_recurence('ABCBC'))
print(recursive_recurence('CABDCC'))
print(recursive_recurence('ABCD'))
print(recursive_recurence('ABCDD'))
print(recursive_recurence('ABCDCDA'))
