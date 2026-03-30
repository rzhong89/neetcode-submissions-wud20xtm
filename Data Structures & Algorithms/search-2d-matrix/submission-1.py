class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = ROWS * COLS - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            row = middle // COLS
            col = middle % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return False


        
