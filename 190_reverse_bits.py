class Solution:
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

#Time complexity: O(1)
#Space complexity: O(1)  
       

        
