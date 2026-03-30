class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min k should be 1
        # max k should be len(piles)
        '''
        So what I'm thinking is that we calculate the left pointer
         to see how many hours it would take to finish the thing,
          the piles, and then we would calculate the same thing 
          for the right pile. If it's less than age, then we would 
          just or no, I don't think we would ever change our left 
          pointer because we want to search for the minimum. So if
           it was greater than age, then we would decrease the right
            pointer to the middle. The time and space complexity for
             this would just be O(log H) or no, O(log length of
             piles). And then some edge cases are if if a pile is
              empty or even or if the pile length is equal to H or
               if H is zero or negative 
        '''

        left = 1
        right = max(piles)
        res = float('infinity')

        while left <= right:
            mid = left + (right - left) // 2

            totalHours = 0

            for n in piles:
                totalHours += math.ceil(n / mid)

            if totalHours > h:
                left = mid + 1
            elif totalHours <= h:
                res = min(res, mid)
                right = mid - 1

        return res

            
