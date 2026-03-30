class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if len(edges) > n - 1:
        #     return False
        
        adjList = defaultdict(list)
        visited = set()

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for n in adjList[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n

        

        