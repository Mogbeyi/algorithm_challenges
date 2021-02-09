def compareTriplets(a, b):
    score_for_a = 0
    score_for_b = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            score_for_a += 1
        elif b[i] > a[i]:
            score_for_b += 1
            
    return [score_for_a, score_for_b]

print(compareTriplets([17, 28, 30], [99, 16, 8]))
print(compareTriplets([5, 6, 7], [3, 6, 10]))
