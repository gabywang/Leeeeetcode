class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        if prices == []:
            return 0
        else:
            minv = max(prices)
        # O(n): keep tracking the min value and the max profit.
        # O(n^2): use two for loops.
        for i in range(len(prices)):
            if prices[i] < minv:
                minv = prices[i]
            elif prices[i] - minv > maxprofit:
                maxprofit = prices[i] - minv
        return maxprofit