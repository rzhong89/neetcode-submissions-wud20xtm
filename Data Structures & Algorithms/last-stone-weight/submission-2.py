import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(heap, stone2 - stone1)
            else:
                heapq.heappush(heap, stone1 - stone2)

        return abs(heap[0]) if heap else 0
            

