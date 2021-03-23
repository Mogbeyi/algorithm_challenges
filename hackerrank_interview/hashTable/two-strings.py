def two_strings(first, second):
    set_of_second = set(second)

    for char in first:
        if char in set_of_second:
            return "YES"

    return "NO"
