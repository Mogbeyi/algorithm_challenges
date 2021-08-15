from collections import Counter

# def getMaxAndMinProduct(A, Q, N, P):
#     ans = []

#     for elem in Q:
#         count = 0

#         for value in A:
#             if value % elem == 0:
#                 count += 1

#         ans.append(count)

#     return ans

def getMaxAndMinProduct(A, Q, N, P):
    max_value = max(A)
    freq_of_A = Counter(A)
    answer = []

    for value in Q:
        count = 0
        result = 1

        for i in range(max_value):
            result = value * i
            if result > max_value:
                break
            if result in freq_of_A:
                count += 1
        answer.append(count)

    return answer

def main():
    N = 6
    A = [2, 4, 9, 15, 21, 20]
    M = 3
    Q = [2, 3, 6, 5, 7]

    print(getMaxAndMinProduct(A, Q, N, M))

main()
