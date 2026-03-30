class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        memo = {}

        if target % 2 != 0:
            return False

        def dfs(i, curr):
            if i == len(nums):
                return curr == target // 2

            if target < 0:
                return False

            if (i, curr) in memo:
                return memo[(i, curr)]

            memo[i] = dfs(i + 1, curr) or dfs(i + 1, curr + nums[i])
            return memo[i]

        return dfs(0, 0)

            


            
            