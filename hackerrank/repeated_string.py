def repeated_string(s, n):
    no_of_a = s.count('a')
    quotient = n // len(s)
    freq_of_a = no_of_a * quotient 
    remainder = n % len(s)

    for char in s[:remainder]:
        if char == 'a':
            freq_of_a += 1

    return freq_of_a
