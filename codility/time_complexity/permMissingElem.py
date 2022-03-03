def solution(A):
    length = len(A) + 1
    real_sum = length * (length + 1) // 2

    return real_sum - sum(A)
