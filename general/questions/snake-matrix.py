def print_snake_matrix(n):
    break_line = 0
    new_line = 1
    diff = n - 1
    is_even = lambda x: x % 2 == 0

    for i in range(1, (n * n) + 1):
        if is_even(new_line):
            print(i + diff, end=" ")
            diff -= 2
        else:
            print(i, end=" ")

        break_line += 1
        if break_line == n:
            diff = n - 1
            new_line += 1
            print("\n")
            break_line = 0

