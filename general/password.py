import string

def get_valid_passwords(data):
    valid_passwords = []

    for password in data:
        if is_valid(password):
            valid_passwords.append(password)

    return valid_passwords 

# def is_valid(password):
#     upper_letters = list(string.ascii_uppercase)
#     lower_letters = list(string.ascii_lowercase)
#     numbers = list('0123456789')
#     chars = list('$#@')

#     return has_char(upper_letters, password) and has_char(lower_letters, password) and has_char(numbers, password) and has_char(chars, password)

# def has_char(chars, password):
#     if ' ' in password:
#         return False

#     exist = False

#     for char in chars:
#        if char in password:
#             exist = True
#             break

#     return exist

def is_valid(password):
    contains_characters = has_char(password)
    contains_upper = contains_characters(string.ascii_uppercase)
    contains_lower = contains_characters(string.ascii_lowercase)
    contains_numbers = contains_characters(list('0123456789'))
    contains_symbols = contains_characters(list('$#@'))

    return contains_upper and contains_lower and contains_numbers and contains_symbols

def has_char(password):
    def contains_char(chars): 
        if ' ' in password:
            return False

        exist = False

        for char in chars:
           if char in password:
                exist = True
                break
        return exist

    return contains_char




def main():
    data = input("Enter passwords separated by comma: ").split(',')
    valid_password = get_valid_passwords(data) 

    print(','.join(valid_password))


main()     
