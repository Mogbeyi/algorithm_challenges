from collections import Counter

def solution(A):
    elements_frequency = Counter(A)

    for elem in A:
        if elements_frequency[elem] % 2 != 0:
            return elem

print(solution([9, 3, 9, 3, 9, 7, 9]))
