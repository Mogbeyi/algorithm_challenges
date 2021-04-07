def recursive_max(arr): 
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        largest = recursive_max(arr[1:])
        print(largest)
        return arr[0] if arr[0] > largest else largest

#print(recursive_max([1,2,3,3,4,5]))
print(recursive_max([1,2,7,10000,8, 3,100]))
