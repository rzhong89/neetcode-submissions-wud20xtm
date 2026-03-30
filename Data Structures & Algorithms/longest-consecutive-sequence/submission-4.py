class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for num in numsSet:
            if num - 1 in numsSet:
                continue
            
            i = num

            while i + 1 in numsSet:
                i += 1
                
            res = max(res, i - num + 1)

        return res