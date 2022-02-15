from collections import Counter

class Solution:
    def sumOfUnique(self, nums):
        num_freq = Counter(nums)
        total = 0
        
        for key, value in num_freq.items():
            if value == 1:
                total += key
                
        return total

print(Solution().sumOfUnique([1,2,3,4,5]))
                
        
        
