class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        def dfs(i, curr):
            if i == len(nums):
                return curr == target // 2

            if target < 0:
                return False

            return dfs(i + 1, curr) or dfs(i + 1, curr + nums[i])

        return dfs(0, 0)

            


            
            