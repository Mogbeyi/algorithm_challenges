def reverse_list(string):
    if len(string) == 0:
        return ''

    return string[-1] + reverse_list(string[:-1])


def test():
    assert reverse_list('') == '' 
    assert reverse_list('love') == 'evol' 
    assert reverse_list('mike') == 'ekim' 

test()
