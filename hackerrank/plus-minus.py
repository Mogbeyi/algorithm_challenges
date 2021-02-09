def plusMinus(arr):
    size = len(arr)
    positive = 0
    negative = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
            
    print(round(positive / size, 6))
    print(round(negative / size, 6))
    print(round(zero / size, 6))

