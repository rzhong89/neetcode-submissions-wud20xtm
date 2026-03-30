class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        fresh = 0

        def add(r, c):
            nonlocal fresh

            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return
            
            fresh -= 1
            q.append((r, c))
            visited.add((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)

            minutes += 1
        
        return max(0, minutes) if fresh == 0 else -1