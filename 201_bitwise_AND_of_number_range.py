class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == right or left==0:
            return left

        shift = 0
        while left != right:
            right = right >> 1
            left = left >>1
            shift += 1

        return left<<shift
        

#Time complexity: O(log n)
#Space complexity: O(1)
        
