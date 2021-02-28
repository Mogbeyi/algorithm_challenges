##bad solution
# def first_recurring_chatacter(string):
#    seen_chars = []
#
#    for char in string:
#        if char not in seen_chars:
#            seen_chars.append(char)
#        else:
#            return char
#
#    return -1

# another bad solution

# def first_recurring_character(string):
#    for i in range(len(string)):
#        if string[i] in string[i + 1:]:
#            return string[i]
#
#    return -1
#


def first_recurring_character(string):
    string_frequency_counter = form_frequency_counter(string)

    for char in string:
        if string_frequency_counter[char] == 2:
            return char

    return -1


def form_frequency_counter(string):
    result = {}

    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(first_recurring_character("ABCA"))
print(first_recurring_character("BCABA"))
print(first_recurring_character("ABC"))
