def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)

    for k in range(n):
        count[A[k]] += 1
    return count

print(counting([1,2,3,4,2], 7))
