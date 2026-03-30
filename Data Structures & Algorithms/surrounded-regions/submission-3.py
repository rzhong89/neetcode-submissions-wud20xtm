class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            if min(r, c) < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != "O":
                return
            
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(board)):
            dfs(r, 0)
            dfs(r, len(board[0]) - 1)

        for c in range(len(board[0])):
            dfs(0, c)
            dfs(len(board) - 1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"