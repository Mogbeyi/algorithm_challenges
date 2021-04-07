def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursive_sum(arr[1:])

def solution(arr, count, total):
    if count == len(arr):
        return total
    return solution(arr, count + 1, total + arr[count])


def tail_recursive_sum(arr):
    return solution(arr, 0, 0)

print(recursive_sum([1, 2, 3, 4]))
print(tail_recursive_sum([1, 2, 3, 4]))
