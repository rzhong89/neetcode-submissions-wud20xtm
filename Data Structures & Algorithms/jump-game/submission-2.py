class Solution:
    def canJump(self, nums: List[int]) -> bool:
         # start backwards at nums[n-2] and see if it can reach [n-1]
         # if it can update goal to current
         # if not then go 1 step back
         # lastly check if goal is 0
        
        goal = len(nums) - 1
        i = len(nums) - 2

        while (goal != 0 and i >= 0):
            if nums[i] + i >= goal:
                goal = i
            i -= 1

        return goal == 0