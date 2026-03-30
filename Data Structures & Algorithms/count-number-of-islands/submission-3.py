class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        expand = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            
            for dr, dc in expand:
                dfs(r + dr, c + dc)
            
            return True
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res