def solution(x, y):
    result = []

    for i in range(x):
        result.append([i * j for j in range(y)])

    return result

def main():
    x, y = input("Enter x and y separated by commas: ").split(',')
    print(solution(int(x), int(y)))

main()
