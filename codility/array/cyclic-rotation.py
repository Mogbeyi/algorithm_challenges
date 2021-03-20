def solution(A, K):
    answer_array = [0] * len(A)

    for i, elem in enumerate(A):
        position = (i + K) % len(A)
        answer_array[position] = elem

    return answer_array

print(solution([3,8,9,7,6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
