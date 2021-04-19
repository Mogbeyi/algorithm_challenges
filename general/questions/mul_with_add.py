def mul_with_add(x, y):
    if y == 0:
        return 0
    return x + mul_with_add(x, y - 1)

print(mul_with_add(2, 4))
print(mul_with_add(3, 2))
