class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        combo = []

        def backtrack(i):
            nonlocal total

            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(combo.copy())
                return

            combo.append(nums[i])
            total += nums[i]
            backtrack(i)

            combo.pop()
            total -= nums[i]
            backtrack(i + 1)

        backtrack(0)
        return res