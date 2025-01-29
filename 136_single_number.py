class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0

        for num in nums:
            a = a ^ num

        return a      

#Space complexity: O(1)
#Time complexity: O(n)  
