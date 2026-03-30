class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)

        for u, v, w in edges:
            adjList[u].append((v, w))

        res = {}
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in res:
                continue
            
            res[n1] = w1

            for n2, w2 in adjList[n1]:
                if n2 not in res:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        for i in range(n):
            if i not in res:
                res[i] = -1

        return res




