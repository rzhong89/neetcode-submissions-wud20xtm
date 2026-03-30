class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        res = []
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        while right < len(nums):
            while heap[0][1] < left:
                heapq.heappop(heap)

            res.append(-heap[0][0])

            left += 1
            right += 1

            if right < len(nums):
                heapq.heappush(heap, (-nums[right], right))

        return res