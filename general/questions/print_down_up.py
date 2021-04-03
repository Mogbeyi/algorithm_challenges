def down_up(string):
    for i in range(-len(string) + 1, len(string)):
        print(string[:abs(i) + 1])

down_up('hello')
