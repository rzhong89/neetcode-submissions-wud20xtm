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

[1, 2, 8, 48]

postfix = 1


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        res[0] = nums[0]
        postfix = 1

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                res[i] = postfix
                break
                
            res[i] = res[i - 1] * postfix
            postfix = postfix * nums[i]

            print(postfix)
            
        return res

