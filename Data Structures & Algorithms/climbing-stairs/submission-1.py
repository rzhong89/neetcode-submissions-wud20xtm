class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        res = 0

        for i in range(n - 1):
            new_total = one + two
            two = one
            one = new_total
        
        return one