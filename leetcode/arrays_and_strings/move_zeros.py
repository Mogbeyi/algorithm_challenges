'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def move_zeros(nums):
    zero_pointer = 0
    zero_count = 0

    for num in nums:
        if num == 0: 
            zero_count += 1
        elif num != 0:
            nums[zero_pointer] = num
            zero_pointer += 1

    for i in range(0, zero_count):
        nums[-(i + 1)] = 0

    return nums

