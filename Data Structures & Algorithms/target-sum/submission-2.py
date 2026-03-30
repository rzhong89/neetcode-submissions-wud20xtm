class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, sum):
            if sum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            if (i, sum) in memo:
                return memo[(i, sum)]

            # add
            memo[(i, sum)] = dfs(i + 1, sum + nums[i])

            #subtract
            memo[(i, sum)] += dfs(i + 1, sum - nums[i])

            return memo[(i, sum)]

        return dfs(0, 0)