def upper_lower_stock(arr):
    return sum(sorted(arr)[1:-1]) / (len(arr) - 2)


print(upper_lower_stock([1,2,3,4]))
