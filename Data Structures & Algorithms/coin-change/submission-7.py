class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, total):
            if total == amount:
                return 0

            if i >= len(coins) or total > amount:
                return float('inf')

            if (i, total) in memo:
                return memo[(i, total)]
            
            use = 1 + dfs(i, total + coins[i])
            skip = dfs(i + 1, total)

            memo[(i, total)] = min(use, skip)
            return memo[(i, total)]
            
        res = dfs(0, 0)
        return -1 if res == float('inf') else res
