class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0
        while n !=0:
            n= n & (n-1)
            ans += 1
        
        return ans

#Time complexity: O(n) (ave: normaly numbers of 1 in n bites)
#Space complexity: O(1)


        
