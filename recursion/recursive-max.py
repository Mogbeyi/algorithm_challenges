'''
RECURSIVE MAX

BASE CASE
if (arr.length == 0):
    raiseError("Array cannot be empty")
elif (arr.lenght == 1):
    max = arr[0]
    return max

INDUCTIVE CASE
max = arr[0] > arr[1] ? arr[0] : arr[1]
'''

def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] if arr[0] > recursive_max(arr[1:]) else recursive_max(arr[1:])

print(recursive_max([1, 3, 4, -99, 10000, -3, 98]))
print(recursive_max([1, 3, 4, -99, 10, -3, 98]))
