class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3: return False
        
        max_value = max(arr)
        if max_value == arr[0] or max_value == arr[-1]:
            return False
        
        i = 0
        while(arr[i] != max_value):
           if arr[i] >= arr[i + 1]:
                return False
            i += 1
            
        j = len(arr) - 1
        while(arr[j] != max_value):
            if arr[j- 1] <= arr[j]:
                return False
            j -= 1
            
        return True
         
