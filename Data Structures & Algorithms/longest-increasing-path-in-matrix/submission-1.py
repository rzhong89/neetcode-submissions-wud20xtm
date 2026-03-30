class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        visited = set()
        memo = {}

        def dfs(i, j, prev):
            nonlocal res

            if min(i, j) < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev or (i, j) in visited:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            visited.add((i,j))

            memo[(i, j)] = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i - 1, j, matrix[i][j]), dfs(i, j - 1, matrix[i][j]), dfs(i, j + 1, matrix[i][j]))
            
            visited.remove((i,j))
            
            res = max(res, memo[(i, j)])
            return memo[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)

        return res