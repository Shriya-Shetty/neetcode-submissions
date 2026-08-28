from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isSafe(row, col, val):
            # check row
            for c in range(9):
                if c != col and board[row][c] == val:
                    return False

            # check column
            for r in range(9):
                if r != row and board[r][col] == val:
                    return False

            # check 3x3 grid
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if (r != row or c != col) and board[r][c] == val:
                        return False

            return True

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if not isSafe(r, c, board[r][c]):
                        return False
        return True
