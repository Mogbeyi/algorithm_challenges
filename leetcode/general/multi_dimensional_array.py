def solution(x, y):
    result = []

    for i in range(x):
        result.append([i * j for j in range(y)])

    return result

def second_solution(x, y):
    result = []

    for i in range(x):
        inner_result = []
        for j in range(y):
            inner_result.append(i * j)
        result.append(inner_result)

    return result

def main():
    x, y = input("Enter x and y separated by commas: ").split(',')
    print(second_solution(int(x), int(y)))

main()
