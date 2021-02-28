def recursive_search(arr, item):
    if len(arr) == 0:
        return False
    elif arr[0] == item:
        return True
    return recursive_search(arr[1:], item)

print(recursive_search([1,2,3,4], 4))
print(recursive_search([1,2,3,5], 4))

