def solution(X, Y, D):
    # write your code in Python 3.6
    diff = abs(X - Y)

    if diff % D == 0:
        return diff // D
    else:
        return diff // D + 1

