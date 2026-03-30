class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')
        memo = {}

        def dfs(i, total, num):
            nonlocal res

            if total == amount:
                return num
            
            if total > amount or i >= len(coins):
                return float('inf')

            if (i, total, num) in memo:
                return memo[(i, total, num)]
            
            memo[(i, total, num)] = min(dfs(i, total + coins[i], num + 1), dfs(i + 1, total, num))
            return memo[(i, total, num)]

        res = dfs(0,0,0)
        return -1 if res == float('inf') else res