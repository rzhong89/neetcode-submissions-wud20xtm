class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = [False] * n
        res = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1
        
        return res