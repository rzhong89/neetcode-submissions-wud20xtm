class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if right - left < 2:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            maxCoins = 0

            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                coins += dfs(left, i) + dfs(i, right)
                maxCoins = max(maxCoins, coins)

            memo[(left, right)] = maxCoins
            return memo[(left, right)]
        
        return dfs(0, len(nums) - 1)