class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, sum):
            if sum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            # add
            res = dfs(i + 1, sum + nums[i])

            #subtract
            res += dfs(i + 1, sum - nums[i])

            return res

        return dfs(0, 0)