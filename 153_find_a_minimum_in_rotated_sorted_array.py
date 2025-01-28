class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right = n - 1
        left = 0

        while left < right:
            middle = (left + right) // 2
            if nums[middle]>nums[right]:
                left = middle +1
            else:
                right = middle 
    
        return nums[left]

#Time complexity: O(log n)
#Space complexity: O(1)

        
