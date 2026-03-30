class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return res
