# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_p = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            else:
                total = prices[i] - min_p
                if total > max_p:
                    max_p = total

        return max_p
