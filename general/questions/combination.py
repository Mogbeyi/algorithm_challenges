def combination(arr):
    result = []
    seen = set()

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if j > i and arr[i] == arr[j]:
                continue
            if arr[i] not in seen:
                result.append([arr[i], arr[j]])

        seen.add(arr[i])

    return result

#print(combination([1,2,3,4]))
print(combination([1,1,2]))
