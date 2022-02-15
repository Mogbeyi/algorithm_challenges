def solution(arr, target):
    if len(arr) == 1 and arr[0] == target:
        return 0
    elif len(arr) == 1 and arr[0] != target:
        return -1

    mid_index = len(arr) // 2   
    first_half = arr[:mid_index]    
    second_half = arr[mid_index:]
    bin_search_first = binary_search(first_half, target)    
    bin_search_second = binary_search(second_half, target)

    if type(bin_search_first) is not int and type(bin_search_second) is not int:
        return -1

    return bin_search_first if bin_search_first else bin_search_second + len(first_half) 

def binary_search(arr, target):
    low = 0
    high = len(arr) -1  

    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

print(solution([4,5,6,7,0,1,2], 2))
print(solution([1, 3], 1))
# print(binary_search([1, 3], 1))

