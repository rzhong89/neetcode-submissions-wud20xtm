class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("infinity")
        left = 0
        right = 0
        windowSum = 0
        
        while right < len(nums):
            windowSum += nums[right]

            while windowSum >= target:
                res = min(res, (right - left + 1))
                windowSum -= nums[left]
                left += 1

            right += 1

        if res == float("infinity"):
            return 0
        else:
            return res
        