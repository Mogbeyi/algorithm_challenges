def recursive_string_length(string):
    if len(string) == 0:
        return 0
    return 1 + recursive_string_length(string[1:])

print(recursive_string_length('hello'))
print(recursive_string_length('hey'))
print(recursive_string_length(''))
