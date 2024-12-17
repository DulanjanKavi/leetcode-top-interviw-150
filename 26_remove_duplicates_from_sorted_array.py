class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        point1 = 0 
        for point2 in range(1, len(nums)): 
            if nums[point2] != nums[point1]: 
                point1 += 1 
                nums[point1] = nums[point2] 
        return point1 + 1
        
#Time complexity: O(n)
#Space complexity: O(1)
