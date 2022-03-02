def solution(x, y, d):
    a = x
    b = y
    c = d
    count = 0

    while a < b:
        count += 1
        a += c

    return count

print(solution(10, 85, 30))
