def skip_string(string, char):
    if len(string) == 0:
        return ''
    elif string[0] == char:
        return skip_string(string[1:], char)
    else:
        return string[0] + skip_string(string[1:], char)

assert (skip_string('baccad', 'a')) == 'bccd'
