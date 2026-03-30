class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[n] = i

            