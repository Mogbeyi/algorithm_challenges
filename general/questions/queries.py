def getMaxAndMinProduct(A, Q, N, P):
    ans = []

    for elem in Q:
        count = 0

        for value in A:
            if value % elem == 0:
                count += 1

        ans.append(count)

    return ans

def main():
    N = 6
    A = [2, 4, 9, 15, 21, 20]
    M = 3
    Q = [2, 3, 5]

    print(getMaxAndMinProduct(A, Q, N, M))

main()
