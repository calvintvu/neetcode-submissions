class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def isValid(lst: List[int]):

            valid = []
            for s in lst:
                if s != ".":
                    valid.append(s)
            return len(valid) == len(set(valid))
        
        # handle rows
        for row in board:
            if not isValid(row):
                return False

        # handle columns
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            if not isValid(temp):
                return False
            temp.clear()
        
        # handle 3x3
        offset = [0, 3, 6]

        for offset1 in offset:
            for offset2 in offset:

                subbox = []

                for i in range(offset1, offset1 + 3):
                    for j in range(offset2, offset2 + 3):

                        subbox.append(board[i][j])
                
                if not isValid(subbox):
                    return False
                subbox.clear()
        
        return True