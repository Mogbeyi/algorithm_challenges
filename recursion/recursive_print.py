def print_recur(lst):
    if not len(lst):
        return
    print(lst[0])
    return print_recur(lst[1:])

def main():
    print_recur([1,2,3,4])

main()
