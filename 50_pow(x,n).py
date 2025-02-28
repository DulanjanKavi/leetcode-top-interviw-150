class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def helper(x,n):
            if x==0:
                return 0
            
            if n==0:
                return 1
            
            res=helper(x,n//2)
            res= res*res

            if n%2 != 0:
                return res*x
            else:
                return res

            


        res=helper(x,abs(n))

        if n>=0:
            return res
        
        else:
            return 1/res

#Time complexity: O(log2(n))
#space complexity:  O(log2(n))


        
        
