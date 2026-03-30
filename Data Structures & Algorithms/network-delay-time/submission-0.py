class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        distance = [float('inf')] * (n + 1)

        for u, v, t in times:
            adj[u].append((v,t))

        def dfs(u, time):
            if time >= distance[u]:
                return

            distance[u] = time

            for nei, w in adj[u]:
                dfs(nei, time + w)

        dfs(k, 0)
        res = max(distance[1:])
        return res if res < float('inf') else -1
