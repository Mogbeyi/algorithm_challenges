def iterative_is_upper(string):
    for char in string:
        if char.isupper():
            return char

    return -1

def recursive_is_upper(string):
    if len(string) == 0:
        return -1 
    elif string[0].isupper():
        return string[0]
    else:
        return recursive_is_upper(string[1:])


print(iterative_is_upper("helloWorld"))
print(iterative_is_upper("HelloWorld"))
print(iterative_is_upper("helloworld"))
print(recursive_is_upper("helloWorld"))
print(recursive_is_upper("HelloWorld"))
print(recursive_is_upper("helloworld"))
