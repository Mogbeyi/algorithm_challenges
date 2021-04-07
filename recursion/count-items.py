def recursive_count(arr):
    if not arr:
        return 0
    return 1 + recursive_count(arr[1:])

def tail_recursive_count(arr):
    
    def solution(arr, idx):
        if idx == len(arr):
            return idx 
        return solution(arr, idx + 1)

    return solution(arr, 0)

print(recursive_count(['a', 'b', 'c', 'd']))
print(tail_recursive_count(['a', 'b', 'c', 'd']))

