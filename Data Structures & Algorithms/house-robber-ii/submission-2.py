class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i, flag):
            if i >= len(nums):
                return 0

            if flag and i == len(nums) - 1:
                return 0

            if (i, flag) in memo:
                return memo[(i, flag)]

            memo[(i, flag)] = max(nums[i] + dfs(i + 2, flag), dfs(i + 1, flag))
            return memo[(i, flag)]
        
        return max(dfs(0, True), dfs(1, False))