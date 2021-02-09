def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0: -1]), sum(arr[1:]))

