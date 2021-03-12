def recursive_max(arr): 
    largest = arr[0]

    if len(arr) == 1:
        return largest
    else:
        largest = arr[0] if arr[0] > arr[1] else arr[1]
        return recursive_max(arr[1:])

print(recursive_max([1,2,3,3,4,5]))
print(recursive_max([1,2,3,3,4,100]))
