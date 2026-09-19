class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        len_row = len(matrix[0])

        while l <= r:

            m = (l + r) // 2

            print(matrix[m][0], matrix[m][len_row - 1])
            if matrix[m][0] > target and matrix[m][len_row - 1] > target:
                r = m - 1
            elif matrix[m][0] < target and matrix[m][len_row - 1] < target:
                l = m + 1
            else:
                
                l2, r2 = 0, len_row
                while l2 <= r2:

                    m2 = (l2 + r2) // 2
                    if matrix[m][m2] == target:
                        return True
                    elif matrix[m][m2] > target:
                        r2 = m2 - 1
                    else:
                        l2 = m2 + 1
                break
        return False