# fib_nums: 0 1 1 2 3 5 8 13
# position: 1 2 3 4 5 6 7 8


def find_fib(n):
    prev, curr = 0, 1
    steps = 1

    while steps < n:
        prev, curr = curr, prev + curr
        steps += 1

    return prev


def test():
    assert find_fib(8) == 13
    assert find_fib(6) == 5
    assert find_fib(1) == 7


test()
