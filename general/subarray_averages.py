def subarray_averages(k, arr):
    averages = []

    for i in range(len(arr) - k + 1):
        total = 0.0

        for i in range(i, i + k):
            total += arr[i]
        averages.append(total / k)

    return averages

print(subarray_averages(5, [1,3,2,6,-1,4,1,8,2]))
