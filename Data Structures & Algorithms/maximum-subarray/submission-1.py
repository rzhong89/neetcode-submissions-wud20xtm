class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):
            # first update current max by taking max(num, cur)
            # then update res with (res, cur)
            cur = max(nums[i], cur + nums[i])
            res = max(cur, res)

        return res