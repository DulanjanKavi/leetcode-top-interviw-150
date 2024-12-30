class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        lo=prices[0]
        hi=prices[0]
        profit=0
        n=len(prices)

        while i< n-1:
            #look what place to buy
            while i + 1 < n and prices[i] >= prices[i+ 1]:
                i+= 1
            lo= prices[i]

            #look what place to sell
            while i + 1 < n and prices[i] <= prices[i+ 1]:
                i += 1
            hi=prices[i]

            profit+=hi-lo
            

        return profit

#Time complexity: O(n)
#Space complexity: O(1)
