'''
I think for this problem, one way we could do it is to just brute 
force. For every index, we would iterate through everything except 
itself and multiply it, but I think that would take O(n^2) time.
I think a way we can optimize this is to create a prefix array so 
that every index is itself times everything before. We could also 
have a postfix array where we do the same thing but go backwards at 
the end of the array. Then we'll loop through our result array that 
we're going to return. For every index, we will multiply it by the 
prefix of i times i minus 1 times the postfix of i plus 1, and then 
we can get what it's supposed to be. 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res