def countingValleys(steps, path):
    # Write your code here
    counter = 0
    number_of_valleys = 0
    
    for i in range(steps):
        if counter == -1 and path[i] == 'U':
            number_of_valleys += 1
        
        if path[i] == 'U':
            counter += 1
        else:
            counter -= 1
            
    return number_of_valleys

assert countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']) == 1
