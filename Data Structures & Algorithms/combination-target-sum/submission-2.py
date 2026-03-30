class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or i >= len(nums):
                return

            combo.append(nums[i])
            dfs(i, total + nums[i])
            combo.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res