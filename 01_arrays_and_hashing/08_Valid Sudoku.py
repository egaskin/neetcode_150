from typing import List

class Solution:
       
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        if self.check_columns_valid(board):
            print("cols valid")
            if self.check_rows_valid(board):
                print("rows valid")
                if self.check_subsquares_valid(board):
                    print("subsquares valid")
                    return True
        return False
    
    def check_columns_valid(self, board):
        # range over all 9 cols
        
        for col_idx in range(9):

            col_set = set()
            # range over 9 rows in this col, unless already in set.
            for row_idx in range(9):
                if board[row_idx][col_idx] != ".":
                    if board[row_idx][col_idx] in col_set:
                        return False
                    col_set.add(board[row_idx][col_idx])
        return True 
    
    def check_rows_valid(self, board):
        # range over all 9 rows
        for row_idx in range(9):

            # range over 9 cols in this row and add to set, unless already in set.
            row_set = set()
            for col_idx in range(9):
                if board[row_idx][col_idx] != ".":
                    if board[row_idx][col_idx] in row_set:
                        return False
                    row_set.add(board[row_idx][col_idx])
        return True 
    
    def check_subsquares_valid(self, board):

        # range over all the subsquares
        all_subsquare_centers = [
            (1,1), (1,4), (1,7),
            (4,1), (4,4), (4,7),
            (7,1), (7,4), (7,7 )
        ]

        for center in all_subsquare_centers:
            center_set = set()
            # range over the rows of the subsquare in context of the full square
            for row_idx in range(center[0] - 1, center[0] + 2):
                for col_idx in range(center[1] - 1, center[1] + 2):
                    print(f"row_idx = {row_idx}, col_idx = {col_idx}, val = {val}")
                    val = board[row_idx][col_idx]
                    if val in center_set:
                        return False
                    if val != ".":
                        center_set.add(val)
        return True