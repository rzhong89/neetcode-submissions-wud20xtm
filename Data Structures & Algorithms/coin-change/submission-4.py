class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0                              # base: 0 coins to reach total=0

        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], 1 + dp[total - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
