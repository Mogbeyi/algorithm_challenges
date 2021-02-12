def staircase(n):
    space, star = n - 1, 1 

    for i in range(1, n + 1):
        print(" " * space, star * "#", sep="")
        space -= 1
        star += 1

staircase(7)
