class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            nonlocal subset

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res