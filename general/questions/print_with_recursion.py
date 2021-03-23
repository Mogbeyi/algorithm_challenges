houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def recursive_print(arr):
    if not arr:
        return 

    print(arr[0])

    return recursive_print(arr[1:])

def tail_recursive_print(arr, i):
    if i == len(arr):
        return

    print(arr[i])

    return tail_recursive_print(arr, i + 1)

tail_recursive_print(houses, 0)
recursive_print(houses)
