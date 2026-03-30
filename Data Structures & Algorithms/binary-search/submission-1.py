class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1
            
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid - 1, nums, target)
        else:
            return self.binary_search(mid + 1, r, nums, target)

        

