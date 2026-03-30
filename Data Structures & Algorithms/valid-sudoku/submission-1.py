class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                val = board[r][c]
                key = [r // 3, c // 3]
                if val in rows[r] or val in cols[c] or val in squares[tuple(key)]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[tuple(key)].add(val)

        return True

