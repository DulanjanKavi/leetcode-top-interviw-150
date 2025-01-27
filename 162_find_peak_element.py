class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_pointer = 0
        right_pointer = len(nums)-1

        while left_pointer <= right_pointer:
            middle = left_pointer + ((right_pointer-left_pointer)//2)

            if middle > 0 and nums[middle] < nums[middle-1]:
                right_pointer = middle-1
            
            elif middle < len(nums) - 1 and nums[middle] < nums[middle+1] :
                left_pointer = middle + 1
            else:
                return middle

#Space complexity: O(n)
#Time complexity: O(log n)
        
