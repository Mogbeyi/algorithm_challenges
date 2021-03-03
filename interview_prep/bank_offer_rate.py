def skip(start, end):
    numbers = list(range(start, end + 1))
    total = 0
    count = 0
    highest_rate = max(numbers)
    lowest_rate = min(numbers)

    for num in numbers:
        if num == lowest_rate or num == highest_rate:
            continue
        total += num
        count += 1

    return total / count

print(skip(1, 9))
