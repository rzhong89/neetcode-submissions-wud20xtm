class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        rob2 = nums[0]
        rob1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            money = max(rob1, nums[i] + rob2)
            rob2 = rob1
            rob1 = money
        
        return rob1