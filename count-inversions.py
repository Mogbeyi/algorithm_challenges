def count_inversions(arr):
    inversions = []
    number_of_inversions = 0

    for i, num in enumerate(arr):
        if i == len(arr) - 1:
            break

        for second_num in arr[i + 1:]:
            if num > second_num:
                number_of_inversions += 1
                inversions.append((num, second_num))

    return number_of_inversions, inversions

def main():
    count, sets = count_inversions([8, 4, 2, 1])
    
    print(count, sets)

main()

