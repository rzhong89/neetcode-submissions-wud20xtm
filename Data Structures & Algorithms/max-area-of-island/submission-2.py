class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(r, c))

        return res