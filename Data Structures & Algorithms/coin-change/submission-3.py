class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][amount] = 0

        
        for i in range(len(coins) - 1, -1 , -1):
            for total in range(amount - 1, -1, -1):
                if total + coins[i] <= amount:
                    dp[i][total] = 1 + dp[i][total + coins[i]]

                dp[i][total] = min(dp[i][total], dp[i + 1][total])

        return dp[0][0] if dp[0][0] != float('inf') else -1