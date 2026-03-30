class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)

        if len(numsSet) < len(nums):
            return True
        else:
            return False

