import inflect
p = inflect.engine()

def letter_to_words(n):
    total = 0

    for num in range(1, n + 1):
        total += len(p.number_to_words(num))

    return total

def test():
    assert letter_to_words(5) == 19

test()
