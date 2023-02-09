def two_sum(nums, target):
    # [2,7,11,15] target = 9

    hashtable = {}

    for i, num in enumerate(nums):
        value = target - num    
        
        if value in hashtable:
            return [hashtable[value], i]
        hashtable[num] = i
