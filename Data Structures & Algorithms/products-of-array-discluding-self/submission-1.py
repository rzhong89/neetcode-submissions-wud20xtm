class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix: multiply over until the end
        # postfix: multiply over until the beginning
        # multiply adjacent cells to get product

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 1, - 1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i + 1] * nums[i]

        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]

        return res


            
        