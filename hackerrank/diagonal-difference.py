def diagonalDifference(arr):
    # Write your code here
    matrix_count = len(arr) - 1
    right_diagonal_sum = 0
    left_diagonal_sum = 0
    
    for i in range(len(arr)):
        right_diagonal_sum += arr[i][i]
        left_diagonal_sum += arr[matrix_count - i][i]
        
    return abs(right_diagonal_sum - left_diagonal_sum)
