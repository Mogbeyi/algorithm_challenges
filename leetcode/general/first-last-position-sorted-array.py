class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        counter, start, end = 0, 0, 0
        found = False
        
        for i, num in enumerate(nums):
            if target == num:
                found = True
                counter += 1
                if counter == 1:
                    start = i
                    end = i
                elif counter > 1:
                    end = i
                    
        if found:
            return [start, end]
        else:
            return [-1, -1]
                    
            
