class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        max_profit=0

        #keep record of minimum price before n th place and get profit with n th price update max_profit if it <profit
        for price in prices:
            if price<min_price:
                min_price=price

            profit=price-min_price

            if profit>max_profit:
                max_profit=profit
            
        return max_profit

#Time complexity: O(n)
#Space complexity: O(1)

       
