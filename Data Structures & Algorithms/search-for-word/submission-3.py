class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(row, col, i):
            if i == len(word):
                return True
            
            if i > len(word) or row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[i] or (row,col) in visited:
                return False

            visited.add((row, col))
            res = backtrack(row + 1, col, i + 1) or backtrack(row - 1, col, i + 1) or backtrack(row, col - 1, i + 1) or backtrack(row, col + 1, i + 1)
            visited.remove((row, col))
            return res



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False
