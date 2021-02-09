def staircase(n):
    space = n - 1
    star = 1

    for i in range(n, 0, -1):
        print(" " * space, star * "#", sep='')
        space -= 1
        star += 1


staircase(6)
