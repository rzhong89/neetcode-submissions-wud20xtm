class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left = 0
        right = len(nums) - 1

        

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return res
        