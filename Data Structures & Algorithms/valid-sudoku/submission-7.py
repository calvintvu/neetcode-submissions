class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False
        
        # check columns
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != '.':
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False
        
        # check 3x3s
        for i in range(9):
            square = []
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] != '.':
                        square.append(board[row][col])
            if len(square) != len(set(square)):
                return False

        return True

