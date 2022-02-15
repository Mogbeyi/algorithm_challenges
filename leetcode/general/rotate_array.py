class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        formula = (i + k) % len(arr)
        """
        
        nums_copy = nums[:]
        size = len(nums)
        
        for i in range(len(nums)):
            nums[(i + k) % size] = nums_copy[i]
            
        
