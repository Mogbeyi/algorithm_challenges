def index_equals_value_search(arr):
  low = 0
  high = len(arr) - 1
  
  while low <= high:
    mid = (low + high) // 2
    
    if mid == arr[mid]:
      return mid
    elif arr[mid] > mid:
      high = mid - 1
    else:
      low = mid + 1
      
  return -1

print(index_equals_value_search([-8, 0, 2, 5]))
