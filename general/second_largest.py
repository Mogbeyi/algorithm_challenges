def find_second_largest(arr):
    largest = arr[0]
    num_store = []

    for num in arr:
        if num > largest:
            largest = num
            num_store.append(num)
    return num_store


print(find_second_largest([1, 4, 3, 5, 2]))
