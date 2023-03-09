def is_palindrome(string):
    if not len(string) or len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False 
    else:
        print(string)
        return is_palindrome(string[1:-1])

print(is_palindrome("eve"))
print(is_palindrome("emme"))
