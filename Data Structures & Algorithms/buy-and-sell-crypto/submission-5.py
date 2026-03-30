class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        if len(prices) == 1:
            return 0

        for r in range(1, len(prices)):
            if prices[left] < prices[r]:
                profit = max(profit, prices[r] - prices[left])
            else:
                left = r

        return profit
            