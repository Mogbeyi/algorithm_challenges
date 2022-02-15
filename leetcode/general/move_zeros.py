def move_zeros(arr):
    result = []

    for val in arr:
        if val != 0:
            result.append(val)

    result.extend([0] * (len(arr) - len(result)))

    return result

print(move_zeros([0,1,0,3,12]))


