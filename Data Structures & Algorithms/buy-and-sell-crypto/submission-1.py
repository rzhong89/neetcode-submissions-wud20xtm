class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        res = 0
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                res = max(res, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1

        return res