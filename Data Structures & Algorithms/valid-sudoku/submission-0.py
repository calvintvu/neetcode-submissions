class Solution:
    
    def isValidRow(self, row: List[str]) -> bool:
        lst = []
        for s in row:
            if s != ".":
                lst.append(s)
        return len(lst) == len(set(lst))
    
    def makeColumnBoard(self, board: List[List[str]]) -> List[List[str]]:
        columns = []
        for i in range(len(board)):
            column = []
            for j in range(len(board[0])):
                column.append(board[j][i])
            columns.append(column)
        return columns

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        c_board = self.makeColumnBoard(board)

        for row in board:
            if not self.isValidRow(row):
                return False

        for col in c_board:
            if not self.isValidRow(col):
                return False
        
        grid = [0, 3, 6]

        for i in grid:
            for j in grid:
                subbox = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        subbox.append(board[r][c])
                print(subbox)
                if not self.isValidRow(subbox):
                    return False
        
        return True

            



