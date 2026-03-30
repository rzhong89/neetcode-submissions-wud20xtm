class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, visited, prevHeight):
            if min(r, c) < 0 or r >= len(heights) or c >= len(heights[0]) or (r, c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # pacific
        for c in range(len(heights[0])):
            dfs(0, c, pac, 0)
            dfs(len(heights) - 1, c, atl, 0)

        for r in range(len(heights)):
            dfs(r, 0, pac, 0)
            dfs(r, len(heights[0]) - 1, atl, 0)

        return [[r, c] for r, c in pac & atl]