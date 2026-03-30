class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxesMap = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                rowSet = rowMap[i]
                colSet = colMap[j]
                boxSet = boxesMap[(math.floor(i / 3), math.floor(j / 3))]

                if board[i][j] in rowSet or board[i][j] in colSet or board[i][j] in boxSet:
                    return False

                rowSet.add(board[i][j])
                colSet.add(board[i][j])
                boxSet.add(board[i][j])

        return True

