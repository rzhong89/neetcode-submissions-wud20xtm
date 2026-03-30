class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if min(r, c) < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))

            res = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1) 
                
            visited.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
            
        return False