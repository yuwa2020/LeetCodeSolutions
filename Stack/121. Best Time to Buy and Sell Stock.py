class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        profit = 0


        for i in range(1, len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
      
            if profit < (prices[i] - lowest):
                profit = prices[i] - lowest
                
            
        return profit