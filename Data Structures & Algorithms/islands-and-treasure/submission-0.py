class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        def addRoom(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        distance = 0

        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = distance

                addRoom(i + 1, j)
                addRoom(i - 1, j)
                addRoom(i, j + 1)
                addRoom(i, j - 1)
            
            distance += 1