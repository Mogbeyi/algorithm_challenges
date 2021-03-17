def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        
        if can_sum(remainder, numbers):
            return True

    return False

print(can_sum(7, [5,3,4,7]))
print(can_sum(7, [2, 4]))
