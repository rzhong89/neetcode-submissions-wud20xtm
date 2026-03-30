class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * 2 * len(nums)
        left = 0
        right = len(nums)

        for i in range((len(nums))):
            res[i] = nums[i]
            res[i + len(nums)] = nums[i]

        return res
